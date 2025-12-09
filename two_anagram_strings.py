def are_anagrams(str1, str2):
    result = True
    if len(str1) != len(str2):
        result = False

    map = dict()
    for char in str1:
        if char in map:
            map[char] += 1
        else:
            map[char] = 1


    for char in str2:
        if char in map:
            map[char] -= 1
        else:
            result = False
            break

    return result


print(are_anagrams("listen", "silent"))