import passwordGenerator as pg

password = []
counter = 0

while counter < 5:
    password.append(pg.GetRandomNumber())

    counter = counter + 1

counter = 0
while counter < 5:
    password.append(pg.GetRadnomChar())

    counter = counter + 1

print(password)

newPassword = pg.GetSampledList(password)

print(newPassword)
