def reverse_array_rec(arr, left, right):
    # Base case: stop when pointers meet or cross
    if left >= right:
        return

    # Swap current pair
    arr[left], arr[right] = arr[right], arr[left]

    # Recurse inward
    print("-----------------------------------------------------")
    print(arr, left, right)
    print("-----------------------------------------------------")
    reverse_array_rec(arr, left + 1, right - 1)


# Wrapper function (for easy use)
def reverse_array(arr):
    reverse_array_rec(arr, 0, len(arr) - 1)
    return arr


# Example
arr = [1, 2, 3, 4, 5]
print("Original:", arr)
reverse_array(arr)
print("Reversed:", arr)
