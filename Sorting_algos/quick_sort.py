import time
import random


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    left_sorted = quick_sort(less)
    right_sorted = quick_sort(greater)
    return left_sorted + [pivot] + right_sorted



print("Starting to create the big array")
big_array = [random.randint(1, 10_000_00) for _ in range(1_000_00)]
print("The big array created")
#print(big_array)

print("quick sort started")
start_time = time.time().real

print(quick_sort([20,2,7,12,15,1,6,8]))

end_time = time.time().real
print(f"Time taken: , {end_time - start_time:.9f} seconds")