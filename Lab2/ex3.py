# 1. A profiler are designed to provide an execution profile for a given program and measures performance of a program. Which shows statistics that describe how often and for how long various parts of the program executed.
"""
2. Profiling is the process of measuring the performance of a program. It can be used to measure the time complexity of a program, and to identify the parts of the program that are taking the most time to execute.
Benchmarking is the process of comparing the performance of a program to other programs, or to a previous version of the program. It can be used to measure the performance of a program, and to identify the parts of the program that are taking the most time to execute.
"""
"""
3. A sample output shows the time taken to execute the function and the number of times the function was called.
    e.g.    4 function calls in 0.000 seconds
    and the functions that are within the function being called. As well with the lines of code being executed.
    the execution time is then split up into the time taken to execute lines of code and other functions.
"""

import timeit
import cProfile
import re

def sub_function(n):
    #sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)
    
def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data
def third_function():
    # third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]


cProfile.run('test_function()')
cProfile.run('third_function()')