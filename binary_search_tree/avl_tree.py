class Node:
    def __init__(self, key, value, height, left=None, right=None):
        self.key = key
        self.value = value
        self.height = height
        self.left = left
        self.right = right

class AVL:
    def __init__(self):
        self.root = None
    
    def height(self, n):
        if n is None:
            return 0
        
        return n.height
    
    def get(self, key):
        return self.get_item(self.root, key)

    def get_item(self, n, k):
        if n is None:
            return None
        
        if n.key > k:
            return self.get_item(n.left, k)
        elif n.key < k:
            return self.get_item(n.right, k)
        else:
            return n.value
    
    def put(self, key, value):
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n, key, value):
        if n is None:
            return Node(key, value, 1)

        if n.key > key:
            n.left = self.put_item(n.left, key, value)
        elif n.key < key:
            n.right = self.put_item(n.right, key, value)
        else:
            n.value = value
            return n
        
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)

    def balance(self, n):
        if self.bf(n) > 1:
            if self.bf(n.left) < 0:
                n.left = self.rotate_left(n.left)
            return self.rotate_right(n)
        elif self.bf(n) < -1:
            if self.bf(n.right) > 0:
                n.right = self.rotate_right(n.right)
            return self.rotate_left(n)
        return n
    
    def bf(self, n):
        return self.height(n.left) - self.height(n.right)

    def rotate_right(self, n):
        x = n.left
        n.left = x.right
        x.right = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x
    
    def rotate_left(self, n):
        x = n.right
        n.right = x.left
        x.left = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x
    
    def delete(self, key):
        self.root = self.del_node(self.root, key)

    def del_node(self, n, k):
        if n == None:
            return None
        if n.key > k:
            n.left = self.del_node(n.left, k)
        elif n.key < k:
            n.right = self.del_node(n.right, k)
        else:
            if n.right == None:
                return n.left
            if n.left == None:
                return n.right
            target = n
            n = self.get_min(target.right) # 오른쪽 자식 최솟값
            n.right = self.del_min(target.right) # target의 오른쪽 자식을 n의 오른쪽 자식으로 설정 -> 두 트리 간섭 X
            n.left = target.left # target의 왼쪽 자식을 n의 왼쪽 자식으로 설정
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)
    
    def del_min(self, n):
        if n.left == None:
            return n.right
        n.left = self.del_min(n.left)   
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)

    def get_min(self, n):
        if n.left == None:
            return n
        return self.get_min(n.left)
    
    def preorder(self, n): # 전위순회
        print(str(n.key),' ', end='')
        if n.left:
            self.preorder(n.left)
        if n.right:
            self.preorder(n.right)

    def inorder(self, n): # 중위순회
        if n.left:
            self.inorder(n.left)
        print(str(n.key), ' ', end='')
        if n.right:
            self.inorder(n.right)

if __name__ == '__main__':
    t = AVL()
    t.put(80, 'A')
    t.put(85, 'B')
    t.put(20, 'C')
    t.put(10, 'D')
    t.put(50, 'E')
    t.put(30, 'F')

    print('전위순회:', end='')
    t.preorder(t.root)
    print('\n중위순회:', end='')
    t.inorder(t.root)
    print('\n80와 50 삭제 후:')
    t.delete(80)
    t.delete(50)
    print('전위순회:', end='')
    t.preorder(t.root)
    print('\n중위순회:', end='')
    t.inorder(t.root)