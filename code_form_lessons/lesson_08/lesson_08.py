import random as r

number = r.randint(1, 1000)
end = False

count = 0

while end == False:
    print("Enter your guess")
    x = input()
    count = count + 1

    if x.isnumeric() == True:
        x = int(x)
        if x > number:
            print("try lower number")
        elif x < number:
            print("try higher number")
        else:
            print("YOU WIN!")
            end = True

print("number of guesses", count)
print("End of code")
