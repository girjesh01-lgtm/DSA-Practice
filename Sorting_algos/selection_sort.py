import time
import random

def selection_sort(arr):
    print("selection sort started")
    start_time = time.time().real
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    end_time = time.time().real
    print(f"Time taken: , {end_time - start_time:.9f} seconds")
    return arr




print("Starting to create the big array")
big_array = [random.randint(1, 10_000) for _ in range(1_000)]
print("The big array created")
print(big_array)
print(selection_sort(big_array))