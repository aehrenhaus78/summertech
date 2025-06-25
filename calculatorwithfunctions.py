def sum (x,y):
    return x+y
def dif(x,y):
    return x-y
def qou(x,y):
    return x-y
def pro(x,y):
    return x*y

while(True):
    x=int(input("enter a number(x)"))
    y=int(input("enter a number(y)"))
    op = input("what operation wold you like to use? [+,-,/,*]")

    if op == "+":
        print(sum(x,y))
    elif op == "-":
        print(dif(x,y))
    elif op == "/":
        print(qou(x,y))
    elif op == "*":
        print(pro(x,y))
    else:
       print("invalid option")
       continue
    answer = input("would you like to go again?(y/n)")
    if answer == "n":
        break
    else:
        continue