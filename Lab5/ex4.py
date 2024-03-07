import timeit
import random
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        if self.head == None:
            self.head = Node(item)
            self.tail = self.head
        else:
            item = Node(item)
            item.next = self.head
            self.head = item
        
    def dequeue(self):
        if self.head is None:  # The queue is empty
            return None
        if self.head == self.tail:  # There's only one item in the queue
            node = self.head
            self.head = self.tail = None
        else:
            node = self.head
            while node.next != self.tail:
                node = node.next
            node.next = None
            self.tail = node
        return node.data

class arrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop()

size = 10000
num_runs = 100

linked_times = []
array_times = []

def generate_task(func):
    linked = linkedQueue()
    array = arrayQueue()
    for _ in range(size):
        random_number = random.random()
        if random_number > 0.7:
            if func == 'linked':
                linked.dequeue()
            else:
                array.dequeue()
        else:
            if func == 'linked':
                linked.enqueue(random_number)
            else:
                array.enqueue(random_number)

for _ in range(num_runs):
    linked_time = timeit.timeit(lambda: generate_task('linked'), number=1)
    array_time = timeit.timeit(lambda: generate_task('array'), number=1)
    print('Linked: ', linked_time, 'Array: ', array_time)
    linked_times.append(linked_time)
    array_times.append(array_time)

plt.hist(linked_times, bins=20, alpha=0.5, label='Linked Queue')
plt.hist(array_times, bins=20, alpha=0.5, label='Array Queue')
plt.legend(loc='upper right')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.title('Distribution of Times for Linked Queue and Array Queue')
plt.show()

# 5, The array queue's enqueue operation is slower (O(n)) due to shifting elements, while its dequeue operation is faster (O(1)) as it removes the last element. 
# Conversely, the linked queue's enqueue operation is faster (O(1)) as it adds a new node to the front, but its dequeue operation is slower (O(n)) as it traverses the queue to find the second to last node.
# But the array is performing faster compared to the linked queue due to the use of inbuilt functions as well as not needing to allocate memory for each node which causes time overhead.