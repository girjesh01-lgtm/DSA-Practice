import time
import random



def insertion_sort(arr):
    print("insertion sort started")
    start_time = time.time().real
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    end_time = time.time().real
    print(f"Time taken: , {end_time - start_time:.9f} seconds")
    return arr






print("Starting to create the big array")
big_array = [random.randint(1, 10_000) for _ in range(1_000)]
print("The big array created")
print(big_array)
print(insertion_sort(big_array))