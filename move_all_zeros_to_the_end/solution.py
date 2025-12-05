def move_all_zeros_to_the_end(arr):
    change_index = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            temp = arr[i]
            arr[i] = 0
            arr[change_index] = temp
            change_index += 1

    return arr




print(move_all_zeros_to_the_end([0, 1, 0, 3, 12, 0, 5]))
arr = [1, 2, 0, 3]
print(move_all_zeros_to_the_end(arr))