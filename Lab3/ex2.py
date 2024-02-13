import sys
import random
import timeit
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Generate array of arrays with randomized elements
average_case = []
for i in range(1,105,5):
    array = []
    j = 5*(i+1)
    for j in range(j):
        array.append(random.randint(1, 100))
    average_case.append(array)

# Test average case is generated correctly
#for i in range(16):
#    print("length of array", str(i+1) + ": " + str(len(average_case[i])))

#array of reversed elements; worst case for bubble sort
worst_case_bubble = []
for i in range(1,105,5):
    array = []
    j = 5*(i+1)
    for j in range(j, 0, -1):
        array.append(j)
    worst_case_bubble.append(array)

#array of reversed elements; worst case for quick sort as well
worst_case_quick = []
for i in range(1,105,5):
    array = []
    j = 5*(i+1)
    for j in range(j, 0, -1):
        array.append(j)
    worst_case_quick.append(array)


#array of arrays where all elements are sorted; best case for bubble sort
best_case_bubble = []
for i in range(1,105,5):
    array = []
    j = 5*(i+1)
    for j in range(j):
        array.append(j)
    best_case_bubble.append(array)

#array of arrays where all elements are sorted; best case for quick sort
best_case_quick = []
for i in range(1, 105, 5):
    array = []
    j = 5 * (i + 1)
    for j in range(j):
        array.append(j)
    best_case_quick.append(array)

average_times_bubble = []
average_times_quick = []
for i in range(len(average_case)):
    average_times_bubble.append(timeit.timeit(lambda: bubble_sort(average_case[i]), number=1))
    average_times_quick.append(timeit.timeit(lambda: quick_sort(average_case[i]), number=1))

worst_times_bubble = []
for i in range(len(worst_case_bubble)):
    worst_times_bubble.append(timeit.timeit(lambda: bubble_sort(worst_case_bubble[i]), number=1))

worst_times_quick = []
for i in range(len(worst_case_quick)):
    worst_times_quick.append(timeit.timeit(lambda: quick_sort(worst_case_quick[i]), number=1))

best_times_bubble = []
for i in range(len(best_case_bubble)):
    best_times_bubble.append(timeit.timeit(lambda: bubble_sort(best_case_bubble[i]), number=1))

best_times_quick = []
for i in range(len(best_case_quick)):
    best_times_quick.append(timeit.timeit(lambda: quick_sort(best_case_quick[i]), number=1))

# Plot the results
plt.scatter(range(1,105,5), average_times_bubble, label='Bubble Sort')
plt.scatter(range(1,105,5), average_times_quick, label='Quick Sort')
plt.title('Average Case Performance')
plt.xlabel('Length of Array')
plt.ylabel('Time(s)')
plt.legend()
plt.savefig("average_case_performance.jpg")
plt.show()

plt.scatter(range(1, 105, 5), worst_times_bubble, label='Bubble Sort')
plt.scatter(range(1, 105, 5), worst_times_quick, label='Quick Sort')
plt.title('Worst Case Performance')
plt.xlabel('Length of Array')
plt.ylabel('Time(s)')
plt.legend()
plt.savefig("worst_case_performance.jpg")
plt.show()

plt.scatter(range(1, 105, 5), best_times_bubble, label='Bubble Sort')
plt.scatter(range(1, 105, 5), best_times_quick, label='Quick Sort')
plt.title('Best Case Performance')
plt.xlabel('Length of Array')
plt.ylabel('Time(s)')
plt.legend()
plt.savefig("best_case_performance.jpg")
plt.show()