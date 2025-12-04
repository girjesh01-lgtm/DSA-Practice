# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(P, Q):
    # Implement your solution here
    total_string_possible = 2 ** len(P)

    # empty dict or map to store the frequencies of the chars

    possible_str = []
    for count in range(total_string_possible):
        arrangement = int(bin(count + 1)[2:], 10)
        combination = ''
        index = len(P)-1
        char_freq = {}
        while True:
            key = P[index] if (arrangement % 10 == 0) else Q[index]
            arrangement//=10
            if (key in char_freq):
                char_freq[key] += 1
            else:
                char_freq[key] = 1

            if (index == 0):
                break
            index -= 1
        print(char_freq)
        possible_str.append(char_freq)

    minimum_number = len(possible_str[0])
    for diction in (possible_str):
        if (len(diction) < minimum_number):
            minimum_number = len(diction)

    return minimum_number



print(solution('axxz', 'yzwy'))