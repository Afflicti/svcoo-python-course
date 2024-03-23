word = ["a", "h", "o", "j"]

correct = []
wrong = []

length = len(word)
end = False

while end == False:
    item = input()
    wrong.append(item)

    x = 0
    while x < length:
        if word[x] == item:
            print("correct")
            correct.append(item)
            wrong.pop(len(wrong) - 1)

        x = x + 1

    print("correct:", correct)
    print("wrong:", wrong)



