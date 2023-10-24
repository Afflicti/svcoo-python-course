x = 10

if x > 5:
    print("> 5")
elif x < 0:
    print("< 0")
else:
    print("< 5, > 0")


print("SIMPLE CALCULATOR") 

print("enter first number", end=" ")
x = int(input())

print("enter operator", end=" ")
c = input()

print("enter second number",end=" ")
y = int(input())

if c == "+":
    print(x + y)

if c == "-":
    print(x - y)

