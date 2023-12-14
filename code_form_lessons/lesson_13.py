def DrawVerticalLine(x):
    print()
    count = 0
    while count < x:
        print("*")
        count = count + 1

def DrawSquare(x):
    count1 = 0
    while count1 < x:
        count2 = 0 
        while count2 < x:
            print("*", end="")
            count2 = count2 + 1
        print()
        count1 = count1 + 1

def DrawRectangle(x, y):
    count1 = 0
    while count1 < x:
        count2 = 0 
        while count2 < y:
            print("*", end="")
            count2 = count2 + 1
        print()
        count1 = count1 + 1

def DrawTriangle1(x):
    print()
    count = 0
    star = "*"
    while count < x:
        print(star)
        count = count + 1
        star = star + "*"



DrawVerticalLine(5)
DrawSquare(5)
DrawRectangle(4, 10)
DrawTriangle1(5) #vyska




