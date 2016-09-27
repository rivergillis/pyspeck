WORDLIST_FILENAME = "words.txt"
with(open(WORDLIST_FILENAME, 'r')) as f:
    content = [x.strip('\n') for x in f.readlines()]
# content is now a list of every word in words.txt
print("Loaded " + str(len(content)) + " words")

inputString = input("Please 'swype' something: ")
possible = []
for word in content:
    if len(word) >= 5:
        prevLetter = ""
        tempString = inputString
        possibleFlag = True
        for letter in word:
            if letter != prevLetter: # get double letters for free
                if letter not in tempString:
                    possibleFlag = False
                    #if (word == 'apple'):
                    #    print(letter + " is not in " + tempString)
                else:
                    #if (word == 'apple'):
                    #    print(str(len(tempString)) + " " + tempString + " " + str(inputString.index(letter)))
                    if (len(tempString) - 1) != tempString.index(letter):
                        tempString = tempString[tempString.index(letter)+1:]
                    else:
                        tempString = ''
                    prevLetter = letter
                
            #tempString = tempString.replace(letter, "")
        if possibleFlag:
            possible.append(word)
            print("**************FOUND " + word)
betterPicks = [x for x in possible if x[0] == inputString[0] and x[-1] == inputString[-1]]
print(betterPicks)
