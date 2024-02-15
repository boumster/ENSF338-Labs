import json
import timeit
import matplotlib.pyplot as plt

def binary_search(arr, x, first_midpoint_ratio=None):
    l = 0
    r = len(arr) - 1

    while l <= r:
        if first_midpoint_ratio is not None:
            mid = l + int((r - l) * first_midpoint_ratio)
            first_midpoint_ratio = None  # So that it's used only for the first iteration
        else:
            mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    return -1

with open('ex7data.json') as f:
        data = json.load(f)
        
# Call the binary_search function with the data array and a value to search for
with open('ex7tasks.json') as f:
    tasks = json.load(f)

midpoints = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
best_midpoints = []

for task in tasks:
    best_time = float('inf')
    best_midpoint = 0

    for midpoint in midpoints:
        time = timeit.timeit(lambda: binary_search(data, task, midpoint), number=100) / 100

        if time < best_time:
            best_time = time
            best_midpoint = midpoint

    best_midpoints.append(best_midpoint)
    print(f'Task: {task}, Best Midpoint: {best_midpoint}')

plt.figure(figsize=(10, 6))
plt.scatter(tasks, best_midpoints)
plt.xlabel('Task')
plt.ylabel('Best Midpoint')
plt.title('Best Midpoint for Each Task')
plt.savefig('scatterplot.png')
plt.show()

# 4. The choice of the initial midpoint does not appear to affect the perfomance of the binary search as the graph does not display the clearest patterns as some of the lowest numbers have the best performance using the highest midpoint and vice versa.
# This could be by chance as the data set is so large and that from the highest midpoint to the lowest midpoint could have perfect divisions to the number that is smaller than the lower midpoint and vice versa.
# Therefore the intial midpoint does not really affect the performance of the binary search.

