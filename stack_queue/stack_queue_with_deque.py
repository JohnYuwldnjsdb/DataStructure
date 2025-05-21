from collections import deque

stack = deque()
stack.append('apple')
stack.append('orange')
stack.append('cherry')
print(stack)
stack.pop()
print(stack)

queue = deque()
queue.append('apple')
queue.append('orange')
queue.append('cherry')
print(queue)
queue.pop()
print(queue)