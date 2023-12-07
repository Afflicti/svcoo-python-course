
##FUNC DEFINITION
def sum(num1, num2):
    print("In function sum()")
    result = num1 + num2

    return result

def sub(num1, num2):
    print("In function sub()")
    result = num1 - num2

    return result

def mul(num1, num2):
    print("In function mul()")
    result = num1 * num2
    return result



##MAIN
print("enter first number:")
input1 = int(input())

print("enter second number:")
input2 = int(input())

print("enter operation:")
operation = input()


if operation == "+":
    print("summary:", sum(input1, input2))
elif operation == "-":
    print("substraction:", sub(input1, input2))
elif operation == "*":
    print("multiplication:", mul(input1, input2))


