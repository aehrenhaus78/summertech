board = []
from random import randrange

def PrintBoard(board):
    print("   A  B  C  D  E  F  G  H  I  J")
    for i in range(10):
        print(i, end = " ")
        for j in range(10):
            print(board[i][j], end ="")
        print( )

def MakeBoard(board):
    for i in range(10):
        board.append([])
        for j in range(10):
            board[i].append("[ ]")




def ValidateXY(board, x, y):
    if y<0 or y>=10 or x<0 or x>=10:
        return False
    return True
    
def ValidatePlacement(board, x, y, direction, shiplength):
    for i in range(shiplength):
        if direction == "left":
            new_x, new_y = x, y - i
        elif direction == "right":
            new_x, new_y = x, y + i
        elif direction == "up":
            new_x, new_y = x - i, y
        elif direction == "down":
            new_x, new_y = x + i, y
        else:
            return False

        if not ValidateXY(board, new_x, new_y) or board[new_x][new_y] != "[ ]":
            return False
    return True

        

def MakeMove(master, view, x, y):

    if master[x][y] == "[0]":
        view[x][y] = "[H]"#hit
    else:
        view[x][y] = "[M]" #miss


def PlaceShip(board, x, y, direction, shiplength):
    if direction == "left":
        for i in range(shiplength):
            board[x][y - i] = "[0]"
    elif direction == "right":
        for i in range(shiplength):
            board[x][y+i] = "[0]"
    elif direction == "down":
        for i in range(shiplength):
            board[x+i][y] = "[0]"
    elif direction == "up":
        for i in range(shiplength):
            board[x-i][y] = "[0]"
    


def LetterToCoordinate(letter):
    if letter=="A":
        return 0
    elif letter=="B":
        return 1
    elif letter=="C":
        return 2
    elif letter=="D":
        return 3
    elif letter=="E":
        return 4
    elif letter=="F":
        return 5
    elif letter=="G":
        return 6
    elif letter=="H":
        return 7
    elif letter=="I":
        return 8
    elif letter=="J":
        return 9
    
    
def CheckWinner(board):
    count = 0
    for i in range(10):
        for j in range(10):
            if board[i][j] == "[0]":
                count=count+1
    if count==17:
        return True
 



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("time to place your ships")
playerBoard=[]
computerBoard=[]
guessingBoard=[]
shipSizes=[2,3,3,4,5]

MakeBoard(playerBoard)
MakeBoard(computerBoard)
MakeBoard(guessingBoard)

placingShips=True
playerTurn=True
computerTurn=True
playing=True

for shipSize in shipSizes:
    placingShips=True
    while(placingShips==True):
        PrintBoard(playerBoard)
        print("the next ship is", shipSize, "spaces")
        col=(input("Select the column for your ship [A-J] "))
        if col in "abcdefghijklmnopqrstuvwxyzKLMNOPQRSTUVWXYZ":
            print("invalid option")
            continue
        col = LetterToCoordinate(col)
        row=int(input("Select row 0-9 "))
        if row<0 or row>9:
            print("invalid option")
            continue
        direction=input("choose a direction:left, right, up, down ")
        if ValidatePlacement(playerBoard, row, col, direction, shipSize):
            PlaceShip(playerBoard, row, col, direction, shipSize)
            PrintBoard(playerBoard)
            placingShips=False

for shipSize in shipSizes:
    # placingShips=True (i fixed it)
    while(placingShips==True):
        row=randrange(10)
        col=randrange(10)

        directions=["up", "down", "left", "right"]
        direction =directions[randrange(0,4)]

        if ValidatePlacement(computerBoard, row, col, direction, shipSize): 
            PlaceShip(computerBoard, row, col, direction, shipSize)
playing = True
while(playing == True):
    # PrintBoard(playerBoard)
    PrintBoard(guessingBoard)
    print("your turn")
    playerTurn=True
    while(playerTurn==True):
        col=input("Select a column to guess [A-J] ")
        if col in "abcdefghijklmnopqrstuvwxyzKLMNOPQRSTUVWXYZ":
            print("invalid option")
            continue
        col = LetterToCoordinate(col)
        row=int(input("Select row 0-9"))
        
        if ValidateXY(computerBoard, row, col)==True:
            MakeMove(computerBoard, guessingBoard, row, col)
            playerTurn=False
    if CheckWinner(guessingBoard)== True:
        playing=False
        print("YOU WIN!!!")
        break
#  make ship sink noticable "[~~x~~]
    computerTurn=True
    while(computerTurn==True):
        PrintBoard(playerBoard)
       #find way tos ave previous computerguess(so it knows to go next to it if it is a hit)
        # else:
        row = randrange(10)
        col = randrange(10)
        if ValidateXY(playerBoard, row, col) == True:
            MakeMove(playerBoard, playerBoard, row, col)
            computerTurn=False

    if CheckWinner(playerBoard)==True:
        playing=False
        print("you lose")
        break

    