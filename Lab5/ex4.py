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
        if self.head == None:
            return None
        else:
            tail = self.tail
            current = self.head
            while current.next != tail:
                current = current.next
            current.next = None
            self.tail = current
            return tail.data