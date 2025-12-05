def intersection(arr1, arr2):
    arr=[]
    first = 0
    second = 0

    while first < len(arr1) and second < len(arr2):
        if arr1[first] == arr2[second]:
            arr.append(arr1[first])
            first += 1
            second += 1
        elif arr1[first] < arr2[second] and first <= len(arr1)-1:
            first += 1
        elif arr1[first] > arr2[second] and second <= len(arr2)-1:
            second += 1

    return arr

print(intersection([1,2,3,4,5,6], [2,4,4,5,8]))
print(intersection([1,1,2,3], [1,1,1,2]))

print(intersection([1,2,5,6,19], [2,4,4,5,8,11,13, 17, 19]))