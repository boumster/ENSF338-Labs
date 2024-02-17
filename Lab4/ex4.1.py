#taking the following code into consideration
def processData(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[i] *= 2

# 1. State and justify what is the best, worst and average case complexity of the processData function.
    #The best case complexity of the processData function is O(n) in the case that the 
    #every element in the list is less than or equal to 5. This is because the function
    #will only iterate through the list once and then return; thus the complexity is linear like
    #linear search. The worst case complexity of the processData function is O(n^2) in the case that
    #every element in the list is greater than 5. This is because the function will iterate through the
    #list once and then iterate through the list again for every element in the list. Thus the complexity
    #is quadratic. The average case complexity of the processData function is O(n^2) because on average,
    #the second loop will run often enough to warrant a quadratic complexity.
                
# 2. Are the average, worst and best case all the same? If not, produce a similar version of the processData function
#    for which the average, worst and best case are the same.
                
def processData_v2(li):
    for i in range(len(li)):
        for j in range(len(li)):
            li[i] *= 2

# see that in this version, the average, worst and best case are all the same. This is because the function
# iterates over each element twice regardless. That is, the removal of the if statement in the first version means that
# the best case complexity matches the average and the worst case complexities of O(n^2).