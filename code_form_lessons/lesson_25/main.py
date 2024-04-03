board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

nextSymbol = True
gameRunning = True

def displayBoard():
    print(board[0] + " | " + board[1] + " | " + board[2] + "      " + "1|2|3")
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5] + "      " + "4|5|6")
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8] + "      " + "7|8|9")

winCombinations = [
    [0, 1, 2],
    [3, 4, 5], 
    [6, 7, 8],
    [0, 3, 6], 
    [1, 4, 7], 
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

def addSymbol():
    global nextSymbol
    choice = int(input("enter tile 1-9:  "))
    if (choice >= 1 and choice <=9) and board[choice-1] == '-':
        board[choice-1] = 'O'
        if (nextSymbol):
            board[choice-1] = 'O'
            nextSymbol = False
        else:
            board[choice-1] = 'X'
            nextSymbol = True

def winCheck():
    global gameRunning 

    for value in board:
            if value == '-':
                gameRunning = True
                break

    for combination in winCombinations:
        if (board[combination[0]] == board[combination[1]] and board[combination[0]] == board[combination[2]]) and board[combination[0]] != '-':
            print(board[combination[0]], " WON!!!")
            gameRunning = False
            break




def startGame():
    displayBoard()
    while gameRunning:
        addSymbol()
        winCheck()
        displayBoard()

startGame()


        
    
                    