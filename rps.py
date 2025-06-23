from random import randint

runAgain=True

while(runAgain):
    user=input("enter [r]ock [p]aper or [s]cissors ")

    computer = randint(1, 4)

    if computer ==1:
        if user =="r":
            print("the computer chose rock, its a tie")    
        elif user=="p":
            print("the computer chose rock, you win")
        elif user =="s":
            print ("the computer chose rock, you lose")

    elif computer ==2:
        if user == "p":
            print("the computer chose paper, its a tie")
        elif user == "r":
            print("the computer chose paper, you lose")
        elif user == "s":
            print("the computer chose paper, you win")

    elif computer == 3:
        if user == "s":
            print("the computer chose scissors, its a tie")
        elif user=="p":
            print("the computer chose scissors, you lose")
        elif user == "r":
            print("the computer chose scissors, you win")

    answer = input("do you want to play again? y/n")
    if answer == "n":
        runAgain=False