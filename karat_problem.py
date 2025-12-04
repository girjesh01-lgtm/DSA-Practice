"""
You are running a classroom and suspect that some of your students are passing around the answer to a multiple-choice question disguised as a random note.

Your task is to write a function that, given a list of words and a note, finds and returns the word in the list that is scrambled inside the note, if any exists. If none exist, it returns the result "-" as a string. There will be at most one matching word. The letters don't need to be in order or next to each other. The letters cannot be reused.

Example:
words = ["baby", "referee", "cat", "dada", "dog", "bird", "ax", "baz"]
note1 = "ctay"
find(words, note1) => "cat"   (the letters do not have to be in order)

note2 = "bcanihjsrrrferet"
find(words, note2) => "cat"   (the letters do not have to be together)

note3 = "tbaykkjlga"
find(words, note3) => "-"     (the letters cannot be reused)

note4 = "bbbblkkjbaby" b - 3 a -0 l 1 k2 y0
find(words, note4) => "baby"

note5 = "dad"
find(words, note5) => "-"

note6 = "breadmaking"
find(words, note6) => "bird"

note7 = "dadaa"
find(words, note7) => "dada"

All Test Cases:
find(words, note1) -> "cat"
find(words, note2) -> "cat"
find(words, note3) -> "-"
find(words, note4) -> "baby"
find(words, note5) -> "-"
find(words, note6) -> "bird"
find(words, note7) -> "dada"

Complexity analysis variables:

W = number of words in `words`
S = maximal length of each word or of the note
"""
words = ["baby", "referee", "cat", "dada", "dog", "bird", "ax", "baz"]

note1 = "ctay"
note2 = "bcanihjsrrrferet"
note3 = "tbaykkjlga"
note4 = "bbbblkkjbaby"
note5 = "dad"
note6 = "breadmaking"
note7 = "dadaa"


def returnWord(words, note):
    # creating map or dictionary
    word_found = '-'
    dict = {}
    # print("in function")
    for letter in note:
        if (dict.get(letter) == None):
            dict[letter] = 1
        else:
            dict[letter] = dict[letter] + 1

    #   print(dict)

    # iterate over the words and check the matching of each word with dict
    for word in words:
        temp_dict = dict.copy()
        length = len(word)
        counter = 0
        for letter in word:
            #print(letter)
            if temp_dict.get(letter) != None and temp_dict.get(letter) > 0:
                #print(temp_dict)
                temp_dict[letter] = temp_dict[letter] - 1
                counter += 1
                #print(f"counter = {counter} length = {length}")
                if (counter == length):
                    word_found = word
                    #print("hello")
                    break

        if (word_found != '-'):
            break

    return word_found


print(returnWord(words, note1))
print(returnWord(words, note2))
print(returnWord(words, note3))
print(returnWord(words, note4))
print(returnWord(words, note5))
print(returnWord(words, note6))
print(returnWord(words, note7))