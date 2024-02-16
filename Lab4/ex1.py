
# Linked List

import timeit
from random import randint
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def newNode(self, x):
        temp = Node(0)
        temp.data = x
        temp.next = None
        return temp

    def middleNode(self, start, last):
        if (start == None):
            return None

        slow = start
        fast = start.next

        while (fast != last):
            fast = fast.next
            if (fast != last):
                slow = slow.next
                fast = fast.next

        return slow

    def binarySearch(self, head, value):
        start = head
        last = None

        while (True):
            mid = self.middleNode(start, last)

            if (mid == None):
                return None

            if (mid.data == value):
                return mid

            elif (mid.data > value):
                start = mid.next

            else:
                last = mid

            if (not last == None or not start == None):
                break

        return None

    def insertNode(self, head, data):
        temp = self.newNode(data)

        if (head == None):
            head = temp
            return temp

        temp.next = head
        head.prev = temp
        head = temp

        return temp

def arrayBinarySearch(arr, value):
    start = 0
    last = len(arr) - 1

    while (start <= last):
        mid = (start + last) // 2

        if (arr[mid] == value):
            return mid

        elif (arr[mid] < value):
            start = mid + 1

        else:
            last = mid - 1

    return -1

# 4. The linked list binary search has a time complexity of O(n) because accessing an element in a linked list is O(n)

sizes = [1000, 2000, 4000, 8000]
linked_list_times = []
array_times = []

for size in sizes:
    array = [i for i in range(size)]
    link = LinkedList()
    head = None
    for i in range(size):
        head = link.insertNode(head, i)
    search_value = randint(0, size - 1)
    linked_list_times.append(timeit.timeit(lambda: link.binarySearch(head, search_value), number=100))
    array_times.append(timeit.timeit(lambda: arrayBinarySearch(array, search_value), number=100))
    print(f"Size: {size}, Linked List Time: {linked_list_times[-1]}, Array Time: {array_times[-1]}")

# Define the form of the function you want to fit
def linear_func(x, a, b):
    return a * x + b

def logarithmic_func(x, a, b):
    return a * np.log(x) + b

# Fit the functions to the data
popt_linear, _ = curve_fit(linear_func, sizes, linked_list_times)
popt_logarithmic, _ = curve_fit(logarithmic_func, sizes, array_times)

# Plot the data and the fitted functions
plt.figure(figsize=(10, 6))
plt.scatter(sizes, linked_list_times, label='Linked List Times')
plt.plot(sizes, linear_func(np.array(sizes), *popt_linear), label='Fitted Linear Function')
plt.scatter(sizes, array_times, label='Array Times')
plt.plot(sizes, logarithmic_func(np.array(sizes), *popt_logarithmic), label='Fitted Logarithmic Function')
plt.legend()
plt.show()
plt.savefig('ex1.png')