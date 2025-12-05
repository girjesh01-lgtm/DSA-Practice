def checkPairSum(arr, K):
    diff_set = set()

    for num in arr:
        if num in diff_set:
            return True
        else:
            diff_set.add(K-num)


    return False


print(checkPairSum([1,2,3,4,6,8], 5))
print(checkPairSum([1,2,3,4,6,8], 9))
print(checkPairSum([1,2,3,4,6,8], 13))
print(checkPairSum([2,3,4,5,6,8], 9))