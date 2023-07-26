print("\n\nCODE MADE BY JAKUB KOPCANSKY - PASSWORD GENERATOR\n\n\n")

import random

# password parameters: 
# 10 chars -> 7 letters, 2 numbers, 1 special 

password = ""

for x in range(7):
    password = password + chr(random.randint(65, 90))

password = password + str(random.randint(0, 9))
password = password + str(random.randint(0, 9))
password = password + random.choice(["*", "!", "?", "/"])

print(password)

password = random.sample(password,len(password))

print("".join(password))


# improvements:
# 1. add small letters
# 2. change password parameters with input
# 3. make your own shuffle function

