import random
import timeit

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListPriorityQueue:
    def __init__(self):
        self.head = None
    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None or data < self.head.data:  
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.data < data:  
                current = current.next
            new_node.next = current.next
            current.next = new_node
    def dequeue(self):
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            return temp

class HeapPriorityQueue:
    def __init__(self):
        self.heap = []

    def heapify(self, arr):
        self.heap = arr
        n = len(self.heap)
        for i in range(n//2 - 1, -1, -1):
            self.heapify_down(i)

    def heapify_down(self, i):
        n = len(self.heap)
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.heap[i] > self.heap[left]:
            smallest = left

        if right < n and self.heap[smallest] > self.heap[right]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest)

    def enqueue(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        parent = (i - 1) // 2
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
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

tasks = []
for i in range(1000):
    prob = random.randint(1,10)
    if prob < 7:
        tasks.append("enqueue")
    else:
        tasks.append("dequeue")

test_list = ListPriorityQueue()
test_heap = HeapPriorityQueue()

def test_time_per_task(tasks, test):
    time_per_task = []
    for task in tasks:
        if task == "enqueue":
            time_per_task.append(timeit.timeit(lambda: test.enqueue(random.randint(1,100)), number=1))
        else:
            time_per_task.append(timeit.timeit(lambda: test.dequeue(), number=1))
        time_average = sum(time_per_task) / len(time_per_task)
        return time_average

def test_overall_time(tasks, test):
    for task in tasks:
        if task == "enqueue":
            test.enqueue(random.randint(1,100))
        else:
            test.dequeue()

print(f"List Implementation overall time: {timeit.timeit(lambda: test_overall_time(tasks, test_list), number=1)}")
print(f"Heap Implementation overall time: {timeit.timeit(lambda: test_overall_time(tasks, test_heap), number=1)}\n")

print(f"ListPriorityQueue average time per task: {test_time_per_task(tasks, test_list)}")
print(f"HeapPriorityQueue average time per task: {test_time_per_task(tasks, test_heap)}")

# The heap implementation from the results seems to be slower than the list implementation.
# Despite the lower complexity, this could be because of several reasons. When dequeueing
# for example, the heap implementation has to re-heapify the array, which is a costly operation.
# The list implementation on the other hand, only has to remove the first element. Another factor
# could be the size of the array. Since our datasets are relatively small, the overhead of the heap's
# constant re-heapifying is costly compared to the list only needing to find the proper spot to insert
# once. 