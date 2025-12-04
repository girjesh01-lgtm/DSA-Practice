import time
import random


def bubble_sort(array):
    print("bubble sort started")
    start_time = time.time().real
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    end_time = time.time().real
    print(f"Time taken: , {end_time - start_time:.9f} seconds")
    return array

print("Starting to create the big array")
big_array = [random.randint(1, 10_000) for _ in range(1_000)]
print("The big array created")
print(big_array)
print(bubble_sort(big_array))