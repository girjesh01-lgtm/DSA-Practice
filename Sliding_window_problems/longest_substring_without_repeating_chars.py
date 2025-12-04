
#longest substring in a given string s without repeating any characters
def length_of_longest_substring(s):
    char_index = {}
    start = 0
    max_len = 0
    end_index = 0
    max_start = 0
    max_end = 0
    for end in range(len(s)):
        #print(f"\n<------start index = {start}")
        #print(f"end index = {end_index}------>\n")
        char = s[end]

        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        else:
            max_start = start
            max_end = end

        char_index[char] = end
        max_len = max(max_len, end - start + 1)
        end_index = end

    print(f"start index = {max_start}")
    print(f"end index = {max_end}")
    #return s[start:end_index-1]
    #return max_len
    return s[max_start:max_end+1], max_len


#s = "abcabcbb"
#s = "pwwkew"
s = "ohvhjdml"
print(f"input string = {s}")
print(length_of_longest_substring(s))  # Output: 3 → "abc"