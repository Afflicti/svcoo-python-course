myList = ["a","h","o","j"]
correct = []
wrong = []
end = False

while end == False :
    x = input()
    y = 0
    wrong.append(x) 

    while y < len(myList):
        if x == myList[y]:
            z = 0
            while z < len(correct):
                if x == correct[z]:
                    print("tohle uz jsi zadal/a")
            
                print("super")
                wrong.pop(len(wrong)-1)
                correct.append(x)
                
                z += 1
        y += 1  
    print(myList)
    print(wrong)
    print(correct) 

