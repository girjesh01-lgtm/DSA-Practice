def reverse_array(array):
    if len(array) <= 1:
        return []

    left, right = 0, len(array) - 1
    while left < right:
        temp = array[left]
        array[left] = array[right]
        array[right] = temp
#        array[left], array[right] = array[right], array[left]

        left += 1
        right -= 1
    return array


arr = [1, 2, 3, 4, 5]
print(arr)
reverse_array(arr)
print(arr)