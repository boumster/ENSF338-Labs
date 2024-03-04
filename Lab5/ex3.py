import random
import timeit
import matplotlib.pyplot as plt

class ArrayStack:
    def __init__(self):
        self.arr = []
    def push(self, value):
        self.arr.append(value)
    def pop(self):
        if not self.arr:
            return None
        else:
            return self.arr.pop()

class Node:
    def __init__(self, value):
        self._value = value
        self._next = None
    def getValue(self):
        return self._value
    def getNext(self):
        return self._next
    def setValue(self, value):
        self._value = value
    def setNext(self, next):
        self._next = next
    def toString(self):
        return str(self._value)
    

class LinkedListStack:
    def __init__(self):
        self._head = None
    def push(self, value):
        node = Node(value)
        node.setNext(self._head)
        self._head = node
    def pop(self):
        if self._head is None:
            return None
        else:
            value = self._head.getValue()
            self._head = self._head.getNext()
            return value
        
def testStack():
    testlist = []
    for i in range(10000):
        which = random.randint(1, 10)
        if which <= 7:
            testlist.append("push()")
        elif which > 7:
            testlist.append("pop()")
    return testlist

def testArr(arr):
    stack = ArrayStack()
    for i in range(len(arr)):
        if (arr[i] == "push()"):
            stack.push(1)
        elif (arr[i] == "pop()"):
            stack.pop()


def testList(arr):
    stack = LinkedListStack()
    for i in range(len(arr)):
        if (arr[i] == "push()"):
            stack.push(1)
        elif (arr[i] == "pop()"):
            stack.pop()
     
ArrayTimes = []
ListTimes = []
for i in range(100):
    taskArr = testStack()
    ListTimes.append(timeit.timeit(lambda: testList(taskArr), number=1))
    ArrayTimes.append(timeit.timeit(lambda: testArr(taskArr), number=1))
    

plt.scatter(range(100), ArrayTimes, label="ArrayStack")
plt.scatter(range(100), ListTimes, label="LinkedListStack")
plt.legend()
plt.show()

# The Array implementation is generally faster than the linked list implementation.
# Despite the fact that both implementations have O(1) time complexity for push and pop operations, the reason for the 
# array implementation's better performance could include a couple of factors. 
# First, the array implementation has a more efficient memory allocation, as it does not require the overhead of creating
# a new node for each element. Second, the array implementation has better cache locality, as the elements are stored
# in contiguous memory locations unlike for a linked list. This means that the array implementation does not have to go through
# the extra overhead of pointer setting, just to set/delete elements.