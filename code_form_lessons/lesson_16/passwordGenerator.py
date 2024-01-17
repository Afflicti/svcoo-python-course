import random

import string

alpha = list(string.ascii_lowercase)

def GetRandomNumber():
    number = random.randint(0, 9)
    
    return number

def GetRadnomChar():
    character = random.choice(alpha)

    return character

def GetZeroOrOne():
    result = random.randint(0,1)

    return result