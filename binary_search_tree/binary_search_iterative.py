arr = [i for i in range(100)]

target = 22

left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right) // 2
    
    if arr[mid] > target:
        right = mid - 1
    elif arr[mid] < target:
        left = mid + 1
    else:
        print(mid, arr[mid])
        break