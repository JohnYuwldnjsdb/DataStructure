class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

def add(item):
    global size, head, tail
    new_node = Node(item, None)
    
    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node

def remove():
    global size, head, tail
    
    if size != None:
        head_item = head.item
        head = head.next
        size -= 1
        if size == 0:
            tail = None
        
        return head_item

def print_list():
    global head
    
    if head is None:
        print("List is empty")
    else:
        current = head
        while current.next != None:
            print(current.item, end=" -> ")
            current = current.next
        print(current.item)

size = 0
head = tail = None
add('apple')
add('orange')
add('cherry')
print_list()
print("Remove:", remove())
print_list()