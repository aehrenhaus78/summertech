runAgain= True


while(runAgain == True):
    no1 =int(input("enter first integer"))
    no2 =int(input("enter second integer"))
    opt =input("what operation would you like to use?")

    sum=no1+no2
    qoutient=no1/no2
    difference=no1-no2
    product=no1*no2


    if opt == "+" or opt == "addition":
        print(no1, "+", no2, "is", sum)
    elif opt =="/" or "division":
        if no2 == 0:
            print("cant be divided by 0")
        else:
            print(qoutient)
    elif opt =="-" or opt =="subtraction":
        print(difference)
    elif opt =="*" or opt =="multiplication":
        print(product)

    answer=input("would you like to calculate again? y/n")
    if answer == "n":
        runAgain = False
    
