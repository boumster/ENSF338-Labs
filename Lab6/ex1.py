# Question 1:
class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        current = self.root
        parent = None

        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right

        if data <= parent.data:
            parent.left = Node(data, parent)
        else:
            parent.right = Node(data, parent)
    
    def search(self, data):
        current = self.root
        while current is not None:
            if data == current.data:
                return current
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return None
    
# Question 2 Part 1:
import numpy as np

sorted_vector = np.arange(1, 10001)

bst = BinarySearchTree()

i = 0
while (i < 10000):
    bst.insert(sorted_vector[i])
    i += 1

# Question 2 Part 2:
import timeit

bst_times = []
for num in sorted_vector:
    time = timeit.timeit(lambda: bst.search(num), number=10) 
    bst_times.append(time/10)

bst_total_time = sum(bst_times)
print("The total time to search all elements using a sorted vector to build a binary tree was: ", bst_total_time)
print("The average time for searching each element using a sorted vector to build a binary tree was: ", bst_total_time / 10000)

# Question 3 Part 1:
import random

random_vector = sorted_vector.copy()
random.shuffle(random_vector)

bst_unsorted = BinarySearchTree()
j = 0
while (j < 10000):
    bst_unsorted.insert(random_vector[j])
    j += 1

# Question 3 Part 2:

bst_unsorted_times = []
for num in random_vector:
    time = timeit.timeit(lambda: bst_unsorted.search(num), number=10) 
    bst_unsorted_times.append(time/10)

bst_unsorted_total_time = sum(bst_unsorted_times)
print("")
print("The total time to search all elements using an unsorted vector to build a binary tree was: ", bst_unsorted_total_time)
print("The average time for searching each element using an unsorted vector to build a binary tree was: ", bst_unsorted_total_time / 10000)

# Question 4:
# Note: This Program takes at least 1 min to run so please be patient when trying to run this file. 
'''
    The approach where we build a binary tree using an unsorted array is much faster. This is because when we create a binary search tree out of 
    a sorted array, then everytime we insert into the tree, we will keep filling up the right post leaf node. This is because each element which
    is being inserted is bigger than the last and thus what we get after the entire insertion process is basically a linked list. And so if we 
    search that linked list we know that time complexity for searching each element is O(n) as we can only start searching from the root of the 
    list. But when building a binary search tree using an unsorted vector we input random values into the tree which ensures it acts more like
    a binary search tree where one node has up to two child nodes. This is also means the search time for searching each element is O(log n) and 
    thus this approach to build a binary search tree using an unsorted vector and then searching that tree is much faster. 
'''





    
