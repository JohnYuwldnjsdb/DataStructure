import random

def selection_sort(a):
    for i in range(len(a) - 1):
        minimum = i
        for j in range(i, len(a)):
            if a[minimum] > a[j]:
                minimum = j
        a[i], a[minimum] = a[minimum], a[i]

a = [i for i in range(1, 101)]
random.shuffle(a)
selection_sort(a)
print(*a)