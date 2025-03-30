import pygame, math, sys

# --- Configuration ---
WIDTH, HEIGHT = 800, 600

# Map / Platform configuration
GROUND_Y = 550  # Ground level y-coordinate
PLATFORM_COLOR = (255, 255, 255)  # white
# The ground is a wide platform.
GROUND_RECT = pygame.Rect(-10000, GROUND_Y, 20000, 50)

# Player shape configuration
BASE_LENGTH = 50          # Base length of the player (in pixels)
GROWTH_PER_BLOCK = 10     # Extra length added per stored block
PLAYER_WIDTH = 20         # Constant width of the rectangle

# Physics and control parameters
THRUST_STRENGTH = 5      # Jump power (impulse magnitude)
GRAVITY = 0.5             # Gravity applied each frame
ROTATION_SPEED = 0.1      # Radians per key press
FPS = 60

# Maximum stack capacity
MAX_STACK_CAPACITY = 10

# Colors (black & white)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# --- Map Functions ---
def create_map():
    """
    Create a list of platforms (pygame.Rect objects).
    The ground platform is included along with several elevated platforms.
    """
    platforms = []
    platforms.append(GROUND_RECT)  # Ground
    # Elevated platforms:
    platforms.append(pygame.Rect(200, 450, 100, 20))
    platforms.append(pygame.Rect(400, 400, 150, 20))
    platforms.append(pygame.Rect(700, 500, 120, 20))
    platforms.append(pygame.Rect(900, 350, 100, 20))
    platforms.append(pygame.Rect(1200, 450, 100, 20))
    platforms.append(pygame.Rect(1500, 300, 200, 20))
    return platforms

def draw_platforms(surface, platforms, camera_offset):
    """
    Draw each platform from the map relative to the camera offset.
    """
    for plat in platforms:
        rect = pygame.Rect(plat.x - camera_offset.x, plat.y - camera_offset.y, plat.width, plat.height)
        pygame.draw.rect(surface, WHITE, rect)

# --- Character Class (Stack Only) ---
class Character:
    def __init__(self, start_pos):
        self.pos = pygame.Vector2(start_pos)
        self.vel = pygame.Vector2(0, 0)
        self.angle = 0  # In radians; 0 means facing right
        self.blocks = []  # Each block represents a jump impulse that increased the stack length

    def get_direction(self):
        """Compute a unit vector pointing in the direction the player is facing."""
        return pygame.Vector2(math.cos(self.angle), math.sin(self.angle))

    def push(self):
        """
        Push (add a block) if under capacity.
        Apply an impulse (jump) in the facing direction.
        The impulse is divided into x and y components based on the player's angle.
        """
        if len(self.blocks) >= MAX_STACK_CAPACITY:
            return  # Stack full: do not push
        direction = self.get_direction()
        thrust = direction * THRUST_STRENGTH
        self.vel += thrust
        self.blocks.append(thrust)

    def pop(self):
        """
        Pop (remove the top block) if available.
        Also apply an impulse (jump) in the facing direction.
        """
        if not self.blocks:
            return
        self.blocks.pop()

    def update(self, platforms):
        # Apply gravity.
        self.vel.y += GRAVITY
        # Update position.
        self.pos += self.vel

        # Check collision against each platform.
        # We use the player's anchor (self.pos) for collision detection.
        for plat in platforms:
            if plat.collidepoint(self.pos.x, self.pos.y) and self.vel.y > 0:
                # Snap the player's position to the top of the platform.
                self.pos.y = plat.top
                # Remove vertical and horizontal speed upon landing.
                self.vel.y = 0
                self.vel.x = 0

    def draw(self, surface, camera_offset, font):
        """
        Draw the player as a rotated rectangle that grows with each added block.
        Each extra block is labeled with its index.
        """
        direction = self.get_direction()
        perp = pygame.Vector2(-math.sin(self.angle), math.cos(self.angle))
        total_length = BASE_LENGTH + len(self.blocks) * GROWTH_PER_BLOCK
        half_width = PLAYER_WIDTH / 2

        # Anchor (tail) is at self.pos; head is at self.pos + direction * total_length.
        tail = self.pos
        head = tail + direction * total_length

        # Compute rectangle corners.
        p1 = tail + perp * half_width
        p2 = tail - perp * half_width
        p3 = head - perp * half_width
        p4 = head + perp * half_width

        # Apply camera offset.
        points = [(p.x - camera_offset.x, p.y - camera_offset.y) for p in [p1, p2, p3, p4]]
        pygame.draw.polygon(surface, WHITE, points)

        # Draw the anchor (tail) as a small circle.
        anchor_screen = (tail.x - camera_offset.x, tail.y - camera_offset.y)
        pygame.draw.circle(surface, WHITE, (int(anchor_screen[0]), int(anchor_screen[1])), 5)

        # Draw indices for each extra block.
        for i in range(len(self.blocks)):
            block_center_distance = BASE_LENGTH + (i + 0.5) * GROWTH_PER_BLOCK
            block_center = tail + direction * block_center_distance
            screen_pos = (block_center.x - camera_offset.x, block_center.y - camera_offset.y)
            index_text = font.render(str(i), True, BLACK)
            text_rect = index_text.get_rect(center=screen_pos)
            surface.blit(index_text, text_rect)

# --- Main Game ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Stack Physics Game with Maps & Landing Reset")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("monospace", 24)

    # Simple menu state.
    game_state = 'menu'
    character = None
    platforms = create_map()  # Create the map

    running = True
    while running:
        if game_state == 'menu':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    # Press S to start.
                    if event.key == pygame.K_s:
                        character = Character((100, GROUND_Y - 50))
                        game_state = 'play'
            screen.fill(BLACK)
            title_text = font.render("Press S to Start", True, WHITE)
            screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 3))
            pygame.display.flip()

        elif game_state == 'play':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    # Rotate the player.
                    if event.key == pygame.K_LEFT:
                        character.angle -= ROTATION_SPEED
                    elif event.key == pygame.K_RIGHT:
                        character.angle += ROTATION_SPEED
                    # Data operations: push (Z) and pop (X)
                    elif event.key == pygame.K_z:
                        character.push()
                    elif event.key == pygame.K_x:
                        character.pop()

            # Update the character with map collisions.
            character.update(platforms)

            # Scrolling camera: center on the character.
            camera_offset = pygame.Vector2(character.pos.x - WIDTH / 2, character.pos.y - HEIGHT / 2)

            screen.fill(BLACK)
            # Draw the map.
            draw_platforms(screen, platforms, camera_offset)
            # Draw the character.
            character.draw(screen, camera_offset, font)

            # Display on-screen instructions and stack count.
            mode_text = font.render("Mode: STACK", True, WHITE)
            instr_text = font.render("Left/Right: Rotate | Z: Push (Jump) | X: Pop (Jump)", True, WHITE)
            cap_text = font.render(f"Stack: {len(character.blocks)}/{MAX_STACK_CAPACITY}", True, WHITE)
            screen.blit(mode_text, (10, 10))
            screen.blit(instr_text, (10, 40))
            screen.blit(cap_text, (10, 70))

            pygame.display.flip()
            clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
