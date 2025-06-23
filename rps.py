from random import randint

runAgain=True

while(runAgain):
    user=input("enter [r]ock [p]aper or [s]cissors ")

    computer = randint(1, 4)

    if computer ==1:
        if user =="r":
            print("its a tie")    
        elif user=="p":
            print("you win")
        elif user =="s":
            print ("you lose")

    elif computer ==2:
        if user == "p":
            print("its a tie")
        elif user == "r":
            print("you lose")
        elif user == "s":
            print("you win")

    elif computer == 3:
        if user == "s":
            print("its a tie")
        elif user=="p":
            print("you lose")
        elif user == "r":
            print("you win")

    answer = input("do you want to play again? y/n")
    if answer == "n":
        runAgain=False