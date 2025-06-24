for i in range(0):
    print("for loop executed")

for i in range(0,4):
    for j  in range(4-i-1):
        print(" ", end="")
    for k in range(i+1):
        print("* ", end="")
    print()
    
for i in range(0,4):
    for j in range(i+1):
        print(" ", end="")
    for k in range(4-i-1):
        print("* ", end="")
    print()