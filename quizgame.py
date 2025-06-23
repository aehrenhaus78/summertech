score = 0
tries = 0


print("What color is the sky?") 
print("a) red b) blue c) purple d) rainbow")
answer = input()
tries =tries+1
if answer =="b" or answer =="blue":
    score = score+1
    print("CORRECT")
else:
    print("You are INCORRECT")
print("your score is now", score, "out of", tries)

print("Who was the first president of the USA.")
print("a) Mickey Mouse b) George Washington c) Abraham Lincoln d) barbie")
answer = input()
tries =tries+1
if answer == "b" or answer == "George Washington":
    score = score+1
    print("Corecct")
else:
    print("WRONG")
print("your score is now", score, "out of", tries)

print("What color is the grass?(double points)")
print("a) red b) purple c) silver d) none of the above")
answer = input()
tries =tries+2
if answer =="d":
    score = score+2
    print("correct")
else :
    print("WRONG")

print("you have now finished with", score, "out of", tries)
if score == 4:
    print("you have won!!!")
else:
    print("you have not reached your full potental please play again")