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
        return current.data
    
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

# 7.1 Reverse function has a time complexity of O(n^2) because i