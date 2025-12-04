# User function Template for python3

# arr    : list of integers denoting the elements of the array
# target : as specified in the problem statement

class Solution:
    def threeSumClosest(self, arr, target):
        # Your Code Here
        arr.sort()
        n = len(arr)

        closest_sum = float('inf')

        for i in range(n - 2):
            left = i + 1
            right = n - 1
            print(f"left {arr[left]}, right {arr[right]}, i {arr[i]}")
            while left < right:
                curr_sum = arr[i] + arr[left] + arr[right]

                # if exact match return immediatly
                if curr_sum == target:
                    return curr_sum

                if (abs(curr_sum - target) < abs(closest_sum - target)) or (
                        abs(curr_sum - target) == abs(closest_sum - target) and curr_sum > closest_sum):
                    closest_sum = curr_sum

                if curr_sum < target:
                    left += 1
                else:
                    right -= 1
                print(f"left {arr[left]}, right {arr[right]}, i {arr[i]}")
        return closest_sum

s = Solution()
print(s.threeSumClosest([-7, 9, 8, 3, 1, 1], 2))