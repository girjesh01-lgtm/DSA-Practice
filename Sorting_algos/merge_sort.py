import time
import random

def merge_sort_new(arr):
    if len(arr) <= 1:
        return arr
    mid = int(len(arr) / 2)
    left = merge_sort_new(arr[:mid])
    right = merge_sort_new(arr[mid:])
    return merge_new(left, right)

def merge_new(left, right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

        result.extend(left[i:])
        result.extend(right[j:])
    return result



def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


print("Starting to create the big array")
big_array = [random.randint(1, 10_000_00) for _ in range(1_000_00)]
print("The big array created")
#print(big_array)

print("merge sort started")
start_time = time.time().real

merge_sort(big_array)

end_time = time.time().real
print(f"Time taken: , {end_time - start_time:.9f} seconds")