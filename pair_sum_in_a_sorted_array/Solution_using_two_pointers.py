def checkPairSum(arr, K):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] + arr[right] == K:
            return True

        elif arr[left] + arr[right] > K:
            right = right - 1

        elif arr[left] + arr[right] < K:
            left = left + 1

    return False



print(checkPairSum([1,2,3,4,6,8], 5))
print(checkPairSum([1,2,3,4,6,8], 9))
print(checkPairSum([1,2,3,4,6,8], 13))
print(checkPairSum([2,3,4,5,6,8], 9))