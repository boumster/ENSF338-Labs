'''
1. This is the code implementation for recursion.

2. Yes it is an example of divide and conquer as it seperates the big number into small subsections until ultimately 
the problem becomes trivial enough to solve easily. 

3. The time complexity of this fibonacci recursion sequence is O(2^n) as func calls upon itself two times within one function.
'''

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

# Question 4 Implementation:
memo = {}
def func_new(n):
    if n in memo:
        return memo[n]
    
    if n == 0 or n == 1:
        return n
    else:
        result = func(n-1) + func(n-2)
        memo[n] = result
        return result

# Question 5:
# The time complexity of this algorithm is O(n) as now each n's result is only computed once.
    
# Question 6: 
import timeit
import matplotlib.pyplot as plt

# Creates a list of number going from 0 to 35
num_list = list(range(36))
normal_times = []
new_times = []
for n in num_list:
    normal_time = timeit.timeit(lambda:func(n), number=1)
    normal_times.append(normal_time)
    new_time = timeit.timeit(lambda: func_new(n), number=1)
    new_times.append(new_time)

plt.scatter(num_list, normal_times)
plt.title('Normal Fibonacci Sequence')
plt.xlabel('Value of n')
plt.ylabel('Time(s)')
plt.savefig("ex1.6.1.jpg")
plt.close()

plt.scatter(num_list, new_times)
plt.title('Optimized Fibonacci Sequence')
plt.xlabel('Value of n')
plt.ylabel('Time(s)')
plt.savefig("ex1.6.2.jpg")

