cart=input("Enter the product\n").split(",")
def add():
    item=input("Enter the item to add\n")
    print("Add item to cart")
    cart.append(item)
    print("Item added to cart")
def removed():
    item=input("Enter the item to remove\n")
    if item in cart:
      cart.remove(item)
      print("Item removed from cart")
    else:
      print("Item not found in cart")
def viewcart():
    print("The items in cart ",cart)
while True:
    ch=int(input("Enter the choice..\n 1.Add item \n 2. Remove item \n 3.view cart  \n 4.empty\n"))
    if ch == 1:
        add()
    elif ch == 2:
        removed()
    elif ch == 3:
        viewcart()
    elif ch == 4:
        cart.clear()
        print("Cart is empty")
    else:
        print("Invalid choice")
        