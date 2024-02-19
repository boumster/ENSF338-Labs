import timeit
import matplotlib.pyplot as plt
import random

def efficient_search(arr, target): #binary search
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2  # Move the calculation of mid inside the loop
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1
#worst case for binary search is when the target does not exist, or on either end of the array; O(logn).
#worst case for linear search is when the target does not exist, or at the end of the array; O(n).

def inefficient_search(arr, target): #linear search
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Generate large sorted input array of 1000 elements
array = [i for i in range(1001)] 


efficient_search_times = []
inefficient_search_times = []
targets = []
for i in range(100): #100 measurements per task
    target = random.randint(0, 1000) #random target
    targets.append(target)
    efficient_search_times.append(timeit.timeit(lambda: efficient_search(array, target), number=1))
    inefficient_search_times.append(timeit.timeit(lambda: inefficient_search(array, target), number=1))


plt.scatter(targets, efficient_search_times, label='efficient_search') #plotting with chosen random targets as x-axis
plt.scatter(targets, inefficient_search_times, label='inefficient_search')
plt.xlabel('Target')
plt.ylabel('Time (s)')
plt.legend()
plt.show()