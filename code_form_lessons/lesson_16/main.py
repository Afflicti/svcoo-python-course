import passwordGenerator as pg


password = ""
counter = 0

print("enter length of password:")
passwordLen = int(input())

while counter < passwordLen:
    choice = pg.GetZeroOrOne()

    if choice == 1:
        randomElemnt = pg.GetRadnomChar()
        password = password + str(randomElemnt)
    else:
        randomElemnt = pg.GetRandomNumber()
        password = password + str(randomElemnt)

    counter = counter + 1

print(password)
