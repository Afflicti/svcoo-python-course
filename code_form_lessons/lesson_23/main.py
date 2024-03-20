import msvcrt

counter = 0
max_len = int(input("Enter maximal length:"))
file = open("log.txt", "a")
key = ''

print("enter your text:  ")
while counter < max_len and key != '*' :
    key = msvcrt.getwche()
    file.write(key)
    counter += 1

file.close()

character = input("\nenter your character:  ")
file = open("log.txt", "r")
myString = file.read()
wordCounter = 0

for i in myString:
    if i == character:
        wordCounter += 1

print("number of ", character, ":   ", wordCounter)












































# import msvcrt
# import os

# file = open("log.txt", "a")
# key = ''
# os.system('cls')
# while key != 'l':
#     key = msvcrt.getwche()
#     os.system('cls')
#     print(key)
#     file.write(key)

# file.close()
