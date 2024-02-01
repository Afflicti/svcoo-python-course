import passwordGenerator as pg

password = []
counter = 0

print("Enter number of numbers:")
numLen = int(input())


while counter < numLen:
    password.append(str(pg.GetRandomNumber()))

    counter = counter + 1

counter = 0
while counter < 5:
    password.append(pg.GetRadnomLowChar())

    counter = counter + 1

counter = 0
while counter < 5:
    password.append(pg.GetRadnomUpChar())

    counter = counter + 1

counter = 0
while counter < 5:
    password.append(pg.GetRadnomSpecialChar())

    counter = counter + 1

print("password before sampeling:")
print(password)

newPassword = pg.GetSampledList(password)


print("password after sampeling:")
print("".join(newPassword))
