def maximum_sum_subarray(arr, k):
    left = 0
    window_sum = 0
    max_sum = float('-inf')   # important to note

    for right in range(len(arr)):
        window_sum += arr[right]

        if right >= k - 1:
            max_sum = window_sum if window_sum > max_sum else max_sum
            window_sum -= arr[left]
            left += 1

    return max_sum


print(maximum_sum_subarray([-1, 2, 3, -5, 4], 2))
