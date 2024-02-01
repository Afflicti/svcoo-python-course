import random
import string

lowAlpha = list(string.ascii_lowercase)
UpAlpha = list(string.ascii_uppercase)
SpecialAlpha = ["!", "@", "#", "%", "&", "*"]

def GetRandomNumber():
    number = random.randint(0, 9)
    
    return number

def GetRadnomLowChar():
    character = random.choice(lowAlpha)

    return character

def GetZeroOrOne():
    result = random.randint(0,1)

    return result

def GetSampledList(password):
    result = random.sample(password, len(password))

    return result

def GetRadnomUpChar():
    character = random.choice(UpAlpha)

    return character

def GetRadnomSpecialChar():
    character = random.choice(SpecialAlpha)

    return character