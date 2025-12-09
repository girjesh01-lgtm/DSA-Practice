from collections import deque


def max_of_all_subarrays_of_given_size(arr, k):
    dq = deque()  # will store INDEXES
    result = []

    for right in range(len(arr)):
        # Remove smaller elements from the BACK
        while dq and arr[dq[-1]] <= arr[right]:
            dq.pop()

        dq.append(right)

        # Remove elements outside the window
        if dq[0] < right - k + 1:
            dq.popleft()

        # When window reaches size k, record the max
        if right >= k - 1:
            result.append(arr[dq[0]])

    return result


#arr = [1, 3, -1, -3, 5, 3, 6, 7]
#k = 3

arr = [5, 4, 3, 2, 1]
k = 3

print(max_of_all_subarrays_of_given_size(arr, k))
