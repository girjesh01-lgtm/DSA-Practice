def longest_substring_without_repeating_character_latest(str):
    left =0
    hashset = set()
    longest_length = 0

    for right in range(len(str)):
        while str[right] in hashset:
            hashset.remove(str[left])
            left+=1

        hashset.add(str[right])
        longest_length = max(longest_length, right - left + 1)

    return longest_length



#str = "abcabcbb"
#str = "bbbbb"
#str = "pwwkew"
#str="a"
#str=""
#str="aa"
#str="ab"
#str="🤖😀😁😂🤣😃😄😁"
str="abbaeabcdef"

print(longest_substring_without_repeating_character_latest(str))