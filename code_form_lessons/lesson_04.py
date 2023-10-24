#TASK NO.1 - print rectangle

rectangle_size_x = 5
rectangle_size_y = 10
counter_x = 0
counter_y = 0

while counter_y < rectangle_size_y:
    while counter_x < rectangle_size_x:
        print("#", end="")
        counter_x = counter_x + 1
    print()
    counter_y = counter_y + 1
    counter_x = 0

print("") 
print("")                          
#TASK NO.2 - print triangle |_\

triangle1_height = 10
stars = ""

counter1 = 0

while counter1 < triangle1_height:
    stars = stars + "*"
    print(stars)
    counter1 = counter1 + 1


