
#           0         1         2
myList = ["Jakub", "Martyn", "Vojta"]

print(myList)

myList.append("Karel")

print(myList)

myList.pop(0)

print(myList)

myList[0] = "Martin"

print(myList)
print(len(myList))


text = []
end = False

while end == False:
    item = input()
    text.append(item)
    if len(text) > 5:
        text.pop(0)
    print(text)

word = ["a", "h", "o", "j"]

length = len(word)
end = False

while end == False:
    item = input()

    x = 0
    while x < length:
        if word[x] == item:
            print("ANO")
        x = x + 1

    
















