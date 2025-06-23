import random

def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

def bubble_sort_optimized(a):
    n = len(a)
    for i in range(n - 1):
        flag = False
        
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                flag = True
        
        if not flag:
            break

a = [i for i in range(1, 101)]
random.shuffle(a)
bubble_sort(a)
print(*a)