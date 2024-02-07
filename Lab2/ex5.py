import timeit
import random
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binary_search(arr, x):
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

sizes = [1000, 2000, 4000, 8000, 16000, 32000]
linear_search_times = []
binary_search_times = []

for size in sizes:
    print(f"Starting size: {size}")  # Print the current size
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
    linear_search_times.append(average_linear_search_time)
    binary_search_times.append(average_binary_search_time)

# Define the form of the function you want to fit
def linear_func(x, a, b):
    return a * x + b

def logarithmic_func(x, a, b):
    return a * np.log(x) + b

# Fit the functions to the data
popt_linear, _ = curve_fit(linear_func, sizes, linear_search_times)
popt_logarithmic, _ = curve_fit(logarithmic_func, sizes, binary_search_times)

# Plot the data and the fitted functions
plt.figure(figsize=(10, 6))
plt.scatter(sizes, linear_search_times, label='Linear Search Times')
plt.plot(sizes, linear_func(np.array(sizes), *popt_linear), label='Fitted Linear Function')
plt.scatter(sizes, binary_search_times, label='Binary Search Times')
plt.plot(sizes, logarithmic_func(np.array(sizes), *popt_logarithmic), label='Fitted Logarithmic Function')
plt.legend()

# Save the plot to a file
plt.savefig("plot.png")

plt.show()

# 4 Linear Function: Represents linear search's O(n) complexity with form y = a*x + b, where a is the time per element and b is the base time.
# Logarithmic Function: Represents binary search's O(log n) complexity with form y = a*log(x) + b, where a is the time per doubling of size and b is the base time.

