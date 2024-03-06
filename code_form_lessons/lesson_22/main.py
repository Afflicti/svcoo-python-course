file = open("text.txt", "r")

counter = 0 
word = input()
myString = file.read()
wordLen = len(word)
correctLen = 0

for character in myString:
    if word[correctLen] == character:
        correctLen = correctLen + 1 
    else:
        correctLen = 0

    if wordLen == correctLen:
        counter = counter + 1
        correctLen = 0

print(counter)

file.close()