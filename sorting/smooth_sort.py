import heapq


def numbersLeonardo(size):
    numbers = [1, 1]
    nextNumber = numbers[-1] + numbers[-2] + 1
    while len(numbers) >= 2 and size > nextNumber:
        numbers.append(nextNumber)
        nextNumber = numbers[-1] + numbers[-2] + 1
    numbers.reverse()
    return numbers
    
    
def arrToHeap(data):  # 배열을 받으면 heap 구조로 바꿈
    leonardoNumbers = numbersLeonardo(len(data))
    listHeaps = []
    m = 0
    for i in leonardoNumbers:
        # 아직 할당 안된 배열이 다음 레오나르도 수보다 크거나 같으면
        if len(data) - m >= i:
            listHeaps.append(data[m: m+i])
            # 할당 안된 부분으로 이동
            m += i
    # 힙 성질 맞추기
    for i in listHeaps:
        heapq.heapify(i)
    # heap은 non-decreasing이기 때문에 뒤집기
    listHeaps.reverse()
    return listHeaps


def countIndexes(i, indexes):
    indexes.append(2*indexes[i]+1)
    indexes.append(2*indexes[i]+2)

    return indexes


def getList(indexPart, heap):
    heapPart = []
    for i in indexPart:
        if i < len(heap):
            heapPart.append(heap[i])

    return heapPart


def heapDivision(heap):
    heapleft = []
    heapright = []
    index = 0
    indexesLeft = [1]
    indexesRight = [2]
    while indexesLeft[-1] < len(heap):

        indexesLeft = countIndexes(index, indexesLeft)

        indexesRight = countIndexes(index, indexesRight)

        index += 1

    heapleft = getList(indexesLeft, heap)
    heapright = getList(indexesRight, heap)

    return heapleft, heapright

# Time Complexity O(n) | O(nlogn) | O(nlogn)
# Space Complexity AUX : O(1), Total : O(n)
def smoothSort(array):
    listHeaps = arrToHeap(array)
    result = []
    heapLeft, heapRight = 0, 0

    while (listHeaps):
        flag = 0
        minIndex = listHeaps.index(min(listHeaps))
        currentRoot = listHeaps[0][0]
        currentMin = listHeaps[minIndex][0]
        heapq.heapreplace(listHeaps[0], currentMin)
        heapq.heapreplace(listHeaps[minIndex], currentRoot)
        if len(listHeaps[0]) > 1:
            heapLeft, heapRight = heapDivision(listHeaps[0])
            flag = 1
        minimum = heapq.heappop(listHeaps[0])
        result.append(minimum)
        listHeaps.pop(0)
        if flag == 1:
            listHeaps.insert(0, heapLeft)
            listHeaps.insert(0, heapRight)
    return result

data = [3,5,1,6,2,3,4,6,7]
print(smoothSort(data))

data = [42, 33, 17, 5, 29, 10]
print(smoothSort(data))