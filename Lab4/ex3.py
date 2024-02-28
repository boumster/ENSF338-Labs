# Question 1:
#   The strategy used to grow the array when full in this case is called over-allocation based on current array size. 
#   This can be seen in lines 60-69: 

#   "This over-allocates proportional to the list size, making room for additional 
#   growth.  The over-allocation is mild, but is enough to give linear-time amortized behavior over a long sequence 
#   of appends() in the presence of a poorly-performing system realloc(). Add padding to make the allocated size multiple of 4.
#   The growth pattern is:  0, 4, 8, 16, 24, 32, 40, 52, 64, 76, ... Note: new_allocated won't overflow because the largest 
#   possible value is PY_SSIZE_T_MAX * (9 / 8) + 6 which always fits in a size_t." 

#   This strategy basically allocates more space in memory than is actually needed so that the program doesnt waste time
#   needed to make an array bigger when a person needs to append something to it. It also over-allocates a small portion 
#   so that the array does not take up a lot of space and the over-allocation process is as efficent and fast as possible.
#   The growth factor is approximately 12.5%. This means that the new size will be 12.5% or 1.125 times larger than the old 
#   size. As such, this mild over-allocation ensures minimized reallocations and avoiding excessive memory waste. 

# Question 2: 
import sys
arr = []
capacity = []
arr.append(0)
capacity.append(sys.getsizeof(arr) // 8)

for i in range(1, 64):
    arr.append(i)
    capacity.append(sys.getsizeof(arr) // 8)
    if capacity[i] != (capacity[i-1]):
        print("The underlying capacity changed when you added the", i+1,"element!")

# The largest array of size S which caused the array to expand had 52 elements. As seen by the above code, when we added the 53rd element, 
# the array had to be expanded to fit the 53rd element.

# Question 3:
import timeit

capacity_arr = [] 
def make_capacity_arr():
    global capacity_arr
    capacity_arr = [4] * 52 # Initializes an array that has 52 elements

def expand_capacity_arr():
    global capacity_arr
    capacity_arr.append(8)

def del_capacity_arr():
    global capacity_arr
    del capacity_arr

changing_capacity = []
for i in range(1000): 
    make_capacity_arr()  
    expand_time = timeit.timeit(lambda: expand_capacity_arr(), number = 1)
    changing_capacity.append(expand_time)
    del_capacity_arr()

# Question 4:
size_arr = [] 
def make_size_arr():
    global size_arr
    size_arr = [4] * 51 # Initializes an array that has 51 elements

def expand_size_arr():
    global size_arr
    size_arr.append(8)

def del_size_arr():
    global size_arr
    del size_arr

changing_size = []
for i in range(1000): 
    make_size_arr()  
    expand_time = timeit.timeit(lambda: expand_size_arr(), number = 1)
    changing_size.append(expand_time)
    del_size_arr()

# Question 5:
import matplotlib.pyplot as plt

# Plotting changing_capacity and changing_size on the same histogram
plt.hist(changing_capacity, bins=20, alpha=0.5, label='Capacity')
plt.hist(changing_size, bins=20, alpha=0.5, label='Size')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.title('Time to append an element to an array')
plt.legend()
plt.show()

# As can be seen in the plot, the time taken for expanding capacity or changing the array size from 52 to 52 was longer 
# than the time taken to change the array from 51 elements to 52 elements. And this makes sense as when python needs to
# extend the memory when I append the 53rd element, it needs to find a new spot in memory to put those 52 elements plus
# the one we just appended on to it. The time taken to grow the array from 51 elements to 52 was much shorter as all
# python had to do was just add it in memory since there was already enough space for the 52 element to be added. 