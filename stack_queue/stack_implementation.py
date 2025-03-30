class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next
    
def push(item):
    global top, size
    top = Node(item, top)
    size += 1

def pop():
    global top, size
    if is_empty():
        print("Stack is empty.")
        return None
    else:
        top_item = top.item
        top = top.next
        size -= 1
        return top_item

def peek():
    if is_empty():
        print("Stack is empty.")
        return None
    else:
        return top.item

def is_empty():
    return size == 0

def print_stack():
    temp = top
    while temp.next != None:
        print(temp.item, end=" -> ")
        temp = temp.next
    print(temp.item)

top = None
size = 0
push('apple')
push('orange')
push('cherry')
print_stack()
print('pop:', pop())
print_stack()