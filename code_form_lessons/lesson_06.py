
print("c1:")
x = int(input())

print("z:")
zn = input()

print("c2:")
y = int(input())

print(x, zn, y)

if zn == "+":
    print(x + y)

if zn == "-":
    print(x - y)

if zn == "*":
    print(x * y)

if zn == "/":
    if y == 0:
        print("not possible to divide with zero")
    else:
        print(x / y)

    



