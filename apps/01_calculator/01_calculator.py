print("\n\nCODE MADE BY JAKUB KOPCANSKY - SIMPLE CALCULATOR\n")

print("Hello user! Please insert your equation...\n")

while True:
    print("Enter first number: \t")
    number1 = float(input())
    print("Choose operation (*, /, +, -): \t")
    operator = str(input())
    print("Enter second number: \t\t")
    number2 = float(input())

    if operator == "+":
        print(number1 + number2)
    elif operator == "-":
        print(number1 - number2)
    elif operator == "*":
        print(number1 * number2)
    elif operator == "/":
        print(number1 / number2)
    else:
        print("Operator not supported!")

    print("\n")


# improvements:
# 1. fix division by 0
# 2. add POW and SQRT
# 3. press 'X' to exit program
# 4. fix number input (char instead of num)
