class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root_val

    def peek(self):
        return self.heap[0] if self.heap else None

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[index] < self.heap[parent]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

if __name__ == "__main__":
    h = MinHeap()
    h.push(5)
    h.push(3)
    h.push(8)
    h.push(1)

    print(h.pop())  # 1
    print(h.pop())  # 3
    print(h.pop())  # 5
    print(h.pop())  # 8
