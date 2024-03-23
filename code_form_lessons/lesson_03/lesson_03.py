
#TASK NUMBER 1
counter = 0
stars = "*"

while counter < 10:
    print(stars)
    stars = stars + "*"
    counter += 1

counter = 0
while counter <= 10:
    print(stars)
    stars = stars[:-1]
    counter += 1



#TASK NUMBER 2
counter1=0
counter2=0
stars="*"

while counter1 <5:
    counter2=0
    while counter2 <30:
        print (stars, end ='')
        counter2 +=1
    counter1 +=1
    print()