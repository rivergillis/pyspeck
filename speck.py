WORDLIST_FILENAME = "words.txt"

def load_wordlist(filename):
    """
    filename: string, the path of a file to be read in containing the list of
    every word to be used for the spellchecker
    returns: list of strings, a list of every string contained in the
    file, stripped of newlines
    """
    with(open(filename, 'r')) as f:
        content = [x.strip('\n') for x in f.readlines()]
    # content is now a list of every word in words.txt
    print("Loaded " + str(len(content)) + " words")
    return content

def isGoodCandidate(input_string, guess_word):
    """
    input_string: string, the user input to be spellchecked
    guess_word: string, the word from the wordlist to be checked for candidacy
    returns: bool, True if the guess is of good length and the beginnings and
    endings of both of the strings match up correctly
    """
    return len(guess_word) >= 5 and input_string[0] == guess_word[0] and input_string[-1] == guess_word[-1]

def speck(input_string, content):
    possible = []
    for word in content:
        if isGoodCandidate(input_string, word):
            prev_letter = ""
            temp_string = input_string
            possible_flag = True
            for letter in word:
                if letter != prev_letter: # get double letters for free
                    if letter not in temp_string:
                        possible_flag = False
                    else:
                        if (len(temp_string) - 1) != temp_string.index(letter):
                            temp_string = temp_string[temp_string.index(letter)+1:]
                        else:
                            temp_string = ''
                        prev_letter = letter
            if possible_flag:
                possible.append(word)
    return possible
print(speck(input("Input: "), load_wordlist(WORDLIST_FILENAME)))
