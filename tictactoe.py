board=[]
for i in range(3):
    temp=[]
    for j in range(3):
        temp.append(" ")
    board.append(temp)
    
# users only get 9 moves total
moves=0
letter = "x"

while(moves <9 and moves >= 0):
        print(" "+ board[0][0]+" | "+ board[0][1]+" | "+ board[0][2])
        print(" ----------")
        print(" "+ board[1][0]+" | "+ board[1][1]+" | "+ board[1][2])
        print(" ----------")
        print(" "+ board[2][0]+" | "+ board[2][1]+" | "+ board[2][2])
        print(" ----------")
    
        row=int(input("enter which row you want to go in"))
        col=int(input("enter which column you want to go in"))
        board[row][col]=letter

        moves=moves+1

        # checking the win
        # winning horizontaly
        if board[0][0]==letter and board[0][1]==letter and board[0][2]==letter:
            print(letter, "won!")
            break
        elif board[1][0]==letter and board[1][1]==letter and board[1][2]==letter:
            print(letter, "won!")
            break
        elif board[2][0]==letter and board[2][1]==letter and board[2][2]==letter:
            print(letter, "won!")
            break

        # winning vertically
        elif board[0][0]==letter and board[1][0]==letter and board[2][0]==letter:
            print(letter, "won!")
            break
        elif board[0][1]==letter and board[1][1]==letter and board[2][1]==letter:
            print(letter, "won!")
            break
        elif board[0][2]==letter and board[1][2]==letter and board[2][2]==letter:
            print(letter, "won!")
            break

        # winning diagnoly
        elif board[0][0]==letter and board[1][1]==letter and board[2][2]==letter:
            print(letter, "won!")
            break
        elif board[0][2]==letter and board[1][1]==letter and board[2][0]==letter:
            print(letter, "won!")
            break
        elif moves == 9:
            print("it's a tie")
        if letter == "x":
            letter = "o"
        else:
            letter = "x"


    

