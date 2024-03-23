def DrawSquare(lenght):
    print()
    x = 0
    while x < lenght:
        y = 0
        while y < lenght:
            print("* ", end="")
            y = y + 1
        
        print()
        x = x + 1
    print()

def DrawRectangle(lenght1, lenght2):
    print()
    x = 0
    while x < lenght1:
        y = 0
        while y < lenght2:
            print("* ", end="")
            y = y + 1
        
        print()
        x = x + 1
    print()

def DrawTriangleLeft(length):
    print()
    stars = "* "
    count = 0
    while count < length:
        print(stars)
        stars = stars + "* "
        count = count + 1
    print()

def DrawTriangleRight(length):
    print()
    stars = "*"
    spaces = ""

    count  = 0
    while count < length:
        spaces = spaces + ("  ")
        count = count + 1

    count = 0
    while count < length:
        print(spaces, stars)
        stars = stars + "*"
        spaces = spaces[:-1]
        count = count + 1
    print()

def DrawTriangleBoth(length):
    print()
    stars = "*"
    spaces = ""

    count  = 0
    while count < length:
        spaces = spaces + ("  ")
        count = count + 1

    count = 0
    while count < length:
        print(spaces, stars)
        stars = stars + "**"
        spaces = spaces[:-1]
        count = count + 1
    print()

DrawSquare(5) 
DrawRectangle(5, 10) 
DrawTriangleLeft(5)
DrawTriangleRight(8)
DrawTriangleBoth(8)