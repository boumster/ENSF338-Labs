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
    
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # If target is not found in the array

# Question 2 Part 1:
import numpy as np
import random

shuffled_vector = np.arange(1, 10001) # sorted Vector
random.shuffle(shuffled_vector) # shuffled the sorted Vector

bst = BinarySearchTree()

i = 0
while (i < 10000):
    bst.insert(shuffled_vector[i]) # Building tree out of shuffled vector
    i += 1

# Question 2 Part 2:
import timeit

bst_times = []
for num in shuffled_vector:
    time = timeit.timeit(lambda: bst.search(num), number=10) 
    bst_times.append(time/10)

bst_total_time = sum(bst_times)
print("The total time to search all elements using a Binary Search Tree was: ", bst_total_time)
print("The average time for searching each element using a Binary Search Tree was: ", bst_total_time / 10000)

# Question 3 Part 1:
sorted_vector = np.sort(shuffled_vector) 

# Question 3 Part 2:
bin_search_times = []
for num in sorted_vector:
    time = timeit.timeit(lambda: binary_search(sorted_vector, num), number=10)
    bin_search_times.append(time/10)

print("")
bin_total_time = sum(bin_search_times)
print("The total time to search all elements using Binary Search was: ", bin_total_time)
print("The average time for searching each element using Binary Search was: ", bin_total_time / 10000)

# Question 4:
'''
Using a Binary Search Tree proved to be the faster method of finding each element rather than using Binary search on a vector. 
Even though both searching methods have a complexity of O(log n), using a binary search tree did prove to be faster. This might 
be because on average the complexity for using a binary search is less than O(log n). In a tree such as the one we made above
only some elements are able to become leaf nodes. The majority of the elements are above and this is because we built a tree out
of an unsorted vector and this ensured that the tree was mostly balanced. Thus, due to a mostly balanced tree, we were able to
search for elements much quicker than using binary search on a sorted vector. 
'''



