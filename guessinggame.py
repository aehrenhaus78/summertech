from random import randint


x=randint(0, 11)
guess = -1




while(guess != x):
    guess =int(input("guess the number I am thinking of."))
    if guess > x:
        print("too high")
    elif guess < x:
        print("too low")

if guess == x:
    print("you won!!")