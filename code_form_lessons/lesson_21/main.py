file = open("text.txt", "r")

counter = 0 
lepsiCounter = 0 
Znak = input()
word = input()
myString = file.read()

for character in myString:
    if Znak == character:
        counter = counter + 1

print(counter)

    




