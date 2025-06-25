import random

def downheap(i, size):
    while 2*i <= size:
        k = 2*i
        if k < size and a[k] < a[k+1]:
            k += 1
        
        if a[i] >= a[k]:
            break
        
        a[i], a[k] = a[k], a[i]
        i = k

def create_heap(a):
    hsize = len(a) - 1
    for i in reversed(range(1, hsize//2+1)):
        downheap(i, hsize)

def heap_sort(a):
    N = len(a) - 1
    for i in range(N):
        a[1], a[N] = a[N], a[1]
        downheap(1, N - 1)
        N -= 1

a = [i for i in range(1, 100)]
random.shuffle(a)
a = [-1] + a
create_heap(a)
heap_sort(a)
print(*a)