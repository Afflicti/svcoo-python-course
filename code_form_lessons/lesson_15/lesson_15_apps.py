import lesson_15_calc as calc

def chooseApp():
    print("1 - calc")
    print("2 - shapes")
    print("3 - game")

    option = input()

    if option == "1":
        calc.calcStart()
    elif option == "2":
        shapes.drawShapes()


    