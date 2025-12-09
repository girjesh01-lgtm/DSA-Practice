def largest_subarray(arr, k):
    max_length = 0
    left = 0
    curr_sum = 0

    for right in range(len(arr)):

        curr_sum += arr[right]

        if curr_sum > k:
            curr_sum -= arr[left]
            left += 1

        if curr_sum == k:
            max_length  = max(max_length, right - left + 1)

    return max_length



arr = [1,2,3,1,1,1,5]
k = 6
print(largest_subarray(arr, k))