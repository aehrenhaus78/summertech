board = []
from random import randrange

def PrintBoard(board):
    print("  A  B  C  D  E  F  G  H  I  J")
    for i in range(1,11):
        print(i, end = "")
        for j in range(1,11):
            print(" * ", end ="")
        print( )

def MakeBoard(board):
    for i in range(10):
        board.append([])
        for j in range(10):
            board[i].append("[ ]")

def PlaceShip(board, x, y, direction, shiplength):
    if direction == "up":
        for i in range(shiplength):
            board[y - i][x] = "[0]"
    elif direction == "down":
        for i in range(shiplength):
            board[y+i][x] = "[0]"
    elif direction == "right":
        for i in range(shiplength):
            board[y][x+i] = "[0]"
    elif direction == "left":
        for i in range(shiplength):
            board[y][x-i] = "[0]"
def MakeMove(master, view, x, y):
    if master[x][y] == "[0]":
        view[x][y] == "[X]"#hit
    else:
        view[x][y] == "[Y]" #miss


def ValidateXY(board, x, y):
    if y<0:
        return False
    elif y>=10:
        return False
    elif x<0:
        return False
    elif x>=10:
        return False
    
def ValidatePlacement(board, x, y, direction, shiplength):
    if direction == "up":
        for i in range(shiplength):
            if ValidateXY(board, x, y - i) and board[x][y] == "[ ]":
                pass
            else:
                return False
            return True
    if direction == "down":
        for i in range(shiplength):
            if ValidateXY(board, x, y +i) and board[x][y] == "[ ]":
                pass
            else:
                return False
            return True
    if direction == "left":
        for i in range(shiplength):
            if ValidateXY(board, x -i, y) and board[x][y] == "[ ]":
                pass
            else:
                return False
            return True
    if direction == "right":
        for i in range(shiplength):
            if ValidateXY(board, x +i, y) and board [x][y] == "[ ]":
                pass
            else:
                return False
            return True

def LetterToCoordinate(letter):
    if letter=="A":
        return 1
    elif letter=="B":
        return 2
    elif letter=="C":
        return 3
    elif letter=="D":
        return 4
    elif letter=="E":
        return 5
    elif letter=="F":
        return 6
    elif letter=="G":
        return 7
    elif letter=="H":
        return 8
    elif letter=="I":
        return 9
    elif letter=="J":
        return 10