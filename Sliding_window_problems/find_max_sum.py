
# find the maximum sum any subarray of size k.
def max_sum_subarray(arr, k):
    window_sum=0
    window_start=0
    max_sum = float('-inf')
    for window_end in range(len(arr)):
        window_sum = window_sum + arr[window_end]
        if window_end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum = window_sum - arr[window_start]
            window_start += 1
    print(f"window_start = {window_start-1}, window_end = {window_end}")

    return max_sum


input_list = [19, 4, 12, 23, 56, 87, 81, 64]

print(f"max_sum = {max_sum_subarray(input_list, 5)}")
print(f"max_sum = {max_sum_subarray([2, 1, 5, 1, 3, 2], 3)}")

[-2, 1, -3, 4, -1, 2, 1, -5, 4]