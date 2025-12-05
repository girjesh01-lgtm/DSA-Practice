def check_if_array_is_sorted(arr):
    if len(arr) <=1:
        return True

    prev = arr[0]
    for i in range(1, len(arr)):
        curr = arr[i]
        if curr >= prev:
            prev = curr
            continue
        else:
            return False

    return True


arr = [1,2,3,3,4,5,6,6,7,8,9,9,10]
print(check_if_array_is_sorted(arr))
#print(check_if_array_is_sorted([1,2,3,4,5,6,7,8,9,10]))
