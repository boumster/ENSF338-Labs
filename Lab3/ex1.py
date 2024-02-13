import sys 
sys.setrecursionlimit(20000)

def merge(arr, low, mid, high):
    left = arr[low:mid+1]
    right = arr[mid+1:high+1]
    left.append(float('inf'))
    right.append(float('inf'))
    i = j = 0
    for k in range(low, high+1):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1


def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)
        print('recursive call')

arr = [8, 42, 25, 3, 3, 2, 27, 3]
merge_sort(arr, 0, len(arr)-1)
print(arr)