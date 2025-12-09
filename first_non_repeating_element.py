def first_non_repeating_element_in_array(arr):
    first_non_repeating_element=None
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1


    for num in arr:
        if freq[num] == 1:
            first_non_repeating_element = num

    return first_non_repeating_element







# arr = [1, 2, 2, 3, 3, 3, 1, 17, 9, 9, 19, 17]   # output will be 19
arr = [1, 2, 2, 3, 3, 3, 1, 17, 9, 9, 19, 17, 19]    # output will be None
print(first_non_repeating_element_in_array(arr))