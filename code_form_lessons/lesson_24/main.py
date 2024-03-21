cinemaRowSize = 3
cinemaSeatSize = 6
cinema = [
    [False, False, False, False, False, False],
    [False, False, False, False, False, False],
    [False, False, False, False, False, False]
]

while True:
    for row in cinema:
        print(row)

    rowChoice = input("Enter row char: ")
    rowChoice = ord(rowChoice) - 65

    seatChoice = input("Enter seat number: ")
    seatChoice = int(seatChoice) - 1

    if rowChoice < cinemaRowSize or seatChoice < cinemaSeatSize:
        if cinema[rowChoice][seatChoice] == False:
            print("Seat was free, we just reserved it for you :)")
            cinema[rowChoice][seatChoice] = True
        else:
            print("Oh no... This seat is already taken")
    



    
    
