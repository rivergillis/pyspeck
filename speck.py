WORDLIST_FILENAME = "words.txt"

def load_wordlist(filename):
    with(open(filename, 'r')) as f:
        content = [x.strip('\n') for x in f.readlines()]
    # content is now a list of every word in words.txt
    print("Loaded " + str(len(content)) + " words")
    return content

def speck(input_string, content):
    possible = []
    for word in content:
        if len(word) >= 5:
            prev_letter = ""
            temp_string = input_string
            possible_flag = True
            for letter in word:
                if letter != prev_letter: # get double letters for free
                    if letter not in temp_string:
                        possible_flag = False
                        #if (word == 'apple'):
                        #    print(letter + " is not in " + tempString)
                    else:
                        #if (word == 'apple'):
                        #    print(str(len(tempString)) + " " + tempString + " " + str(inputString.index(letter)))
                        if (len(temp_string) - 1) != temp_string.index(letter):
                            temp_string = temp_string[temp_string.index(letter)+1:]
                        else:
                            temp_string = ''
                        prev_letter = letter
                #tempString = tempString.replace(letter, "")
            if possible_flag:
                possible.append(word)
                print("**************FOUND " + word)
    better_picks = [x for x in possible if x[0] == input_string[0] and x[-1] == input_string[-1]]
    return better_picks

print(speck(input("Input: "), load_wordlist(WORDLIST_FILENAME)))
