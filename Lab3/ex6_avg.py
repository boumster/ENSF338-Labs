import random
import timeit
import matplotlib.pyplot as plt

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binary_search(arr, x):
    quicksort(arr, 0, len(arr) - 1)
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot_index = random.randrange(low, high)
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]  # Move pivot to end
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
linear_avg = []
binary_w_quicksort = []


for size in sizes:
    numbers = [x for x in range(size)]
    random.shuffle(numbers)
    time = timeit.timeit(lambda: linear_search(numbers, size), number=100) / 100
    linear_avg.append(time)
    time = timeit.timeit(lambda: binary_search(numbers, size), number=100) / 100
    binary_w_quicksort.append(time)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(sizes, linear_avg, label='Linear Search')
plt.plot(sizes, binary_w_quicksort, label='Binary Search')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.legend()

# Save the plot as a PNG image
plt.savefig('ex6_avg.png')