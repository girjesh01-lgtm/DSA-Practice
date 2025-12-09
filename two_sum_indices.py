def two_sum(arr, k):
    dictionary = dict()

    for index in range(len(arr)):
        if k-arr[index] in dictionary:
            return [dictionary[k-arr[index]], index]
        else:
            dictionary[arr[index]] = index

    return []



nums = [2,7, 11, 15]
target = 17

print(two_sum(nums, target))