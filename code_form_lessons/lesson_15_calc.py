def add(num1, num2):
    return num1 + num2

def mul(num1, num2):
    return num1 * num2

def calcStart():
    num1 = int(input())
    operation = input()
    num2 = int(input())
    result = 0

    if operation == "*":
        result = mul(num1, num2)
    elif operation == "+":
        result = add(num1, num2)

    print(result)
        
