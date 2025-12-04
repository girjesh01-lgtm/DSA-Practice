# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    binary_array = []
    temp_number = N
    if(temp_number == 0):
        return 0
    while(True):
        if (temp_number %2 == 0):
            binary_array.insert(0,0)
            temp_number = temp_number/2
        else:
            binary_array.insert(0,1)
            if(temp_number == 1):
                break
            temp_number = (temp_number-1)/2

    max_length = 0
    start_index = 0
    end_index = 0
    print(binary_array)
    if len(binary_array) >=3 :
        for i in range(len(binary_array)) :
            if(binary_array[i] == 1):
                end_index = i
                temp_length = end_index-start_index-1
                max_length = max_length if max_length > temp_length else temp_length
                start_index = i
            else:
                end_index = i


    return max_length


print(solution(32))