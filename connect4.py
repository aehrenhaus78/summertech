board = []
for i in range(7):
    spot = []
    for j in range(7):
        spot.append("[ ]")
    board.append(spot)

moves=0
turn="[x]"
tracker=[6,6,6,6,6,6,6]
win = False

for i in range(7):
    for j in range(7):
        print(board[i][j], end="")
    print()

while(moves<49 and moves>=0 and win==False):
    col=int(input("Choose a column 0-6."))

    if col<0 or col>6 or tracker[col]<0:
        print("invalid column try again")
        continue

    row = tracker[col]
    board[row][col]=turn
    tracker[col] = tracker[col]-1
    moves=moves+1

     
    for i in range(7):
        for j in range(7):
            print(board[i][j], end="")
        print()

# checking win horizontally
    for i in range(7):
        for j in range(4):
            if board[i][j]==turn and board[i][j+1]==turn and board[i][j+2]==turn and board[i][j+3]==turn:
                print(" ", turn, "wins!!!")
                win = True
          
               
# checking win vetically
    for i in range(4):
        for j in range(7):
            if board[i][j]==turn and board[i+1][j]==turn and board[i+2][j]==turn and board[i+3][j]==turn:
                print(" ", turn, "wins!!!")
                win = True
               
             
# checking win diagnally
    for i in range(4):
        for j in range(4):
            if board[i][j]==turn and board[i+1][j+1]==turn and board[i+2][j+2]==turn and board[i+3][j+3]==turn:
                print(" ", turn, "wins!!!")
                win = True
               
                
    for i in range(3,7):
        for j in range(4):
            if board[i][j]==turn and board[i-1][j+1]==turn and board[i-2][j+2]==turn and board[i-3][j+3]==turn:
                print(" ", turn, "wins!!!")
                win = True
                
  
                
    if turn == "[x]":
        turn = "[o]"
    else:
        turn = "[x]"
    
if moves == 49 and win == False:
    print("Its a tie")