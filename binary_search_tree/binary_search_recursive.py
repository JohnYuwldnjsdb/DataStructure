arr = [i for i in range(100)]

def search(left, right, target):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] > target:
        return search(left, mid - 1, target)
    elif arr[mid] < target:
        return search(mid + 1, right, target)
    else:
        return mid

print(search(0, len(arr)-1, 22))