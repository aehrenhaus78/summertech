# cart = ["banana", "apple", "cucumber"]
# print(cart[0])
# cart[2] = "pineapple"
# print(cart)
# print(cart[len(cart)-1])


cart = []

while(True):
    answer = input("would you like too (a)dd or (r)emove items in your cart or (n)o?")
    if answer == "a":
        item = input("what would you like to put in your cart?")
        cart.append(item)
        print(cart)
    elif answer == "n":
        print("ok, you have these items in your cart:", cart)
        break
    elif answer == "r":
        print(cart)
        item = input("What would you like to remove?")
        if item not in cart:
            print(item, "not found.")
        else:
            cart.remove(item)
            print("cart updated", cart)
    else:
        print("invalid option")
        break