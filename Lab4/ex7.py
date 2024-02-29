class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singlyLinked:

    def __init__(self):
        self.head = None

    def newNode(self, x):
        temp = Node(0)
        temp.data = x
        temp.next = None
        return temp

    def insert_head(self, data):
        temp = self.newNode(data)
        temp.next = self.head
        self.head = temp
    
    def insert_tail(self, data):
        temp = self.newNode(data)
        if self.head is None:
            self.head = temp
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = temp
    
    def get_size(self):
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        return size
    
    def get_element_at_pos(self, pos):
        current = self.head
        for i in range(pos):
            current = current.next
        return current
    
    def reverse(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size()-1, -1, -1):
            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode.data)
            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.next = currNewNode
            prevNode = currNewNode
        self.head = newhead

# 7.1 Reverse function has a time complexity of O(n^2) because before the for loop self.get_size() is called which has a time complexity of O(n)
        # and inside the for loop, self.get_element_at_pos() is called which has a time complexity of O(n)
        # so the time complexity of the reverse function is O(n^2) = 0(n) * O(n)

    def optimizedReverse(self):
        prevNode = None
        currNode = self.head

        while currNode is not None:
            nextNode = currNode.next  # Temporarily store the next node
            currNode.next = prevNode  # Reverse the link
            prevNode = currNode  # Move prevNode one step forward
            currNode = nextNode  # Move currNode one step forward

        self.head = prevNode  # Set the head to the last node
    
# 7.2 The optimizedReverse function has a time complexity of O(n) because it only has one while loop that iterates through the linked list
        
import timeit

sizes = [1000, 2000, 3000, 4000]
reversed_times = []
optimized_times = []

for size in sizes:
    link = singlyLinked()
    for i in range(size):
        link.insert_head(i)
    reversed_time = timeit.timeit(lambda: link.reverse(), number=100)
    reversed_times.append(reversed_time)
    optimized_time = timeit.timeit(lambda: link.optimizedReverse(), number=100)
    optimized_times.append(optimized_time)
    print(f"Size: {size}, Reverse: {reversed_time}, Optimized: {optimized_time}")