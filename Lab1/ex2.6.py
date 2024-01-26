from functools import reduce
import operator
import timeit

def fact(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

def fact_list_comprehension(num):
    ans = []
    ans = [ans[-1] for i in range(1, num+1) if not ans.append(i*ans[-1] if ans else 1)]
    return ans[-1]

elapsed_time = timeit.timeit(lambda: fact(100), number=1000)
print(f"Time taken for fact: {elapsed_time} seconds")
elapsed_time = timeit.timeit(lambda: fact_list_comprehension(100), number=1000)
print(f"Time taken for fact_list_comprehension: {elapsed_time} seconds")
