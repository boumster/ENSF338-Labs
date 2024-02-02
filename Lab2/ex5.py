import timeit
import random

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r-1) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

sizes = [1000, 2000, 4000, 8000, 16000, 32000]

for size in sizes:
    total_binary_search_time = 0
    total_linear_search_time = 0
    for _ in range(1000):  # Repeat the process 1000 times
        data = sorted([random.random() for _ in range(size)])  # Create a sorted vector of 'size' elements
        random_number = random.choice(data)  # Pick a random element in the vector
        binary_search_time = timeit.timeit(lambda: binary_search(data, random_number), number=100)
        linear_search_time = timeit.timeit(lambda: linear_search(data, random_number), number=100)
        total_binary_search_time += binary_search_time
        total_linear_search_time += linear_search_time
    average_binary_search_time = total_binary_search_time / 1000  # Compute the average time
    average_linear_search_time = total_linear_search_time / 1000  # Compute the average time
    print(f"Size: {size}, Average Binary Search Time: {average_binary_search_time}, Average Linear Search Time: {average_linear_search_time}")


