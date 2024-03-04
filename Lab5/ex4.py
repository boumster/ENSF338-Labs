import timeit
import random

class arrayQueue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item): # Add item to the front of the queue
        new_array = [item]
        for item in self.queue:
            new_array.append(item)
        self.queue = new_array

    def dequeue(self): # Remove item from the end of the queue
        return self.queue.pop()
    
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
        
size = 10000

linked = linkedQueue()
array = arrayQueue()

def generate_task(func):
    for i in range(size):
        random_number = random.random()
        if random_number > 0.7:
            func.dequeue()
        else:
            func.enqueue(random_number)

print("Linked Queue: ", timeit.timeit(lambda: generate_task(linked), number=100))
print("Array Queue: ", timeit.timeit(lambda: generate_task(array), number=100))