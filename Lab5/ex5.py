class CircularQueueArray:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = self.tail = -1
    def enqueue(self, data):
        if (self.tail + 1) % self.size == self.head:
            print("enqueue None")
            return
        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
            print("Enqueued item: ", data)
        else:
            self.tail = (self.tail + 1) % self.size
            self.queue[self.tail] = data
            print("Enqueued item: ", data)
    def dequeue(self):
        if (self.head == -1):  
            print("dequeue None")
            return
        temp = self.queue[self.head]
        if (self.head == self.tail):  
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.size
        print(f"dequeue {temp}")
        return temp
    def peek(self):
        if self.head == -1:
            print("peek None")
            return None
        print(f"peek {self.queue[self.head]}")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueueLinkedList:
    def __init__(self, size):
        self.size = size
        self.curr_size = 0
        self.head = self.tail = Node(None)
    def enqueue(self, data):
        if (self.curr_size == self.size):
            print("enqueue None")
            return
        elif (self.head.data == None):
            self.head.data = data
        else:
            temp = Node(data)
            temp.next = self.head
            self.tail.next = temp
            self.tail = temp
        self.curr_size += 1
        print("Enqueued item: ", data)
    def dequeue(self):
        if (self.curr_size == 0):
            print("dequeue None")
            return
        temp = self.head.data
        if (self.curr_size == 1):
            self.head.data = None
            self.tail.data = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self.curr_size -= 1
        print(f"dequeue {temp}")
        return temp
    def peek(self):
        if (self.curr_size == 0):
            print("peek None")
            return
        print(f"peek {self.head.data}")

Array = CircularQueueArray(10)
List = CircularQueueLinkedList(10)

Array.peek() # peek None
List.peek() # peek None
Array.dequeue() # dequeue None
List.dequeue() # dequeue None
print("\n")

Array.enqueue(1) # Enqueued item:  1
List.enqueue(1) # Enqueued item:  1
Array.peek() # peek 1
List.peek() # peek 1
print("\n")

Array.enqueue(2) # Enqueued item:  2
List.enqueue(2) # Enqueued item:  2
print("\n")

Array.enqueue(3) # Enqueued item:  3
List.enqueue(3) # Enqueued item:  3
print("\n")

Array.enqueue(4) # Enqueued item:  4
List.enqueue(4) # Enqueued item:  4
print("\n")

Array.enqueue(5) # Enqueued item:  5
List.enqueue(5) # Enqueued item:  5
print("\n")

Array.enqueue(6) # Enqueued item:  6
List.enqueue(6) # Enqueued item:  6
print("\n")

Array.enqueue(7) # Enqueued item:  7
List.enqueue(7) # Enqueued item:  7
print("\n")

Array.enqueue(8) # Enqueued item:  8
List.enqueue(8) # Enqueued item:  8
print("\n")

Array.enqueue(9) # Enqueued item:  9
List.enqueue(9) # Enqueued item:  9
print("\n")

Array.enqueue(10) # Enqueued item:  10
List.enqueue(10) # Enqueued item:  10
print("\n")

Array.enqueue(11) # enqueue None
List.enqueue(11) # enqueue None
print("\n")

Array.dequeue() # dequeue 1
List.dequeue() # dequeue 1
Array.peek() # peek 2
List.peek() # peek 2
print("\n")

Array.dequeue() # dequeue 2
List.dequeue() # dequeue 2
Array.peek() # peek 3
List.peek() # peek 3
print("\n")

Array.dequeue() # dequeue 3
List.dequeue() # dequeue 3
Array.peek() # peek 4
List.peek() # peek 4