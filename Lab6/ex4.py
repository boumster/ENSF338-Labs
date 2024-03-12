import random

class heap:
    def __init__(self):
        self.heap = []

    def heapify(self, arr):
        self.heap = arr
        n = len(self.heap)
        # Start from the last non-leaf node
        for i in range(n//2 - 1, -1, -1):
            self.heapify_down(i)

    def heapify_down(self, i):
        n = len(self.heap)
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Check if left child exists and is greater than root
        if left < n and self.heap[i] < self.heap[left]:
            largest = left

        # Check if right child exists and is greater than root
        if right < n and self.heap[largest] < self.heap[right]:
            largest = right

        # Change root if needed
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            # Heapify the root
            self.heapify_down(largest)
    def enqueue(self, item):
        # Add the new item to the end of the heap
        self.heap.append(item)
        # Heapify up from the last index in the heap
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        # Get the index of the parent node
        parent = (i - 1) // 2
        # If the child node is larger than the parent node, swap them
        if i > 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            # Heapify up from the parent node
            self.heapify_up(parent)

    def dequeue(self):
        length = len(self.heap)
        if length == 0:
            return None
        if length == 1:
            return self.heap.pop()
        self.heap[0], self.heap[length - 1] = self.heap[length - 1], self.heap[0]
        value = self.heap.pop()
        self.heapify_down(0)
        return value


test_sorted = heap()
test_sorted.heapify([6, 4, 5, 3, 2, 1])
print("Using sorted array:")
print("Heapify: ", test_sorted.heap) # [6, 4, 5, 3, 2, 1]
print("Dequeue: ", test_sorted.dequeue()) # 6
print("Heap after dequeue: ", test_sorted.heap) # [5, 4, 1, 3, 2]
test_sorted.enqueue(7)
print("Heap after enqueue(7): ", test_sorted.heap) # [7, 4, 5, 3, 2, 1]

print("\nEmpty heap: ")
test_empty = heap()
test_empty.heapify([])
print("Heapify: ",test_empty.heap) # []
print("Dequeue: ", test_empty.dequeue()) # None
test_empty.enqueue(1)
print("Heap after enqueue(1): ", test_empty.heap) # [1]

print("\nRandom heap: ")
test_real = heap()
test_real.heap = [i for i in range(1, 21)]
random.shuffle(test_real.heap)
test_real.heapify(test_real.heap)
print("Heapify: ",test_real.heap) # no guarantee of exact order due to shuffle, but in general, 
                                                 # the heap should maintain properties of a max heap.
print("Dequeue: ", test_real.dequeue()) # 20
print("Heap after dequeue: ", test_real.heap) # 19 should be at the root of the heap now.
test_real.enqueue(21)
print("Heap after enqueue(21): ", test_real.heap) # 21 should be at the root of the heap.