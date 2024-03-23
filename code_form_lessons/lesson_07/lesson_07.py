print("CALCULATOR BY JAKUB")

end = False

while end == False:
    print("enter 1st number: ", end="")
    number01 = float(input())

    print("enter operation: ", end="")
    operation = input()

    print("enter 2nd number: ", end="")
    number02 = float(input())

    print(number01, operation, number02)

    if operation == "+":
        print(number01 + number02)

    elif operation == "-":
        print(number01 - number02)

    elif operation == "*":
        print(number01 * number02)

    elif operation == "/":
        if number02 == 0:
            print("0 is invalid")
        else:
            print(number01 / number02)

    elif operation == "^":
        result = number01
        i = 1
        while i < number02:
            result = result * number01    
            i = i + 1

        print(result)

    print("Do you want to continue? (x)")
    option = input()
    if option == "x":
        end = True
    







