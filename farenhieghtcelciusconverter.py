
def ctof(temp):
    return temp*(9/5)+32
def ftoc (temp):
    return (temp-32)*(5/9)

while(True):
    unit=input("orignal value unit:(c/f)")
    temp = int(input("tempature in degrees c"+unit +":"))
    if unit == "c":
        print(temp, "degrees farenheit is equal to" , ctof(temp))
    elif unit == "f":
        print(temp, "degrees celcius is equal to" , ftoc(temp))
    else:
        print("invalid unit")
        continue
    answer= input("would you like to go again? y/n")
    if answer=="n":
        break
    