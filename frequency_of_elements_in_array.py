def freq_of_elements_in_array(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1


    return freq






arr = [1, 2, 2, 3, 3, 3]
print(freq_of_elements_in_array(arr))