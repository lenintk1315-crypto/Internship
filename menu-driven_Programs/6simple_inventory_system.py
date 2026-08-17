def add_inventory(add_stock,add_quantity,dict_inventory):
    if add_stock in dict_inventory:
        dict_inventory[add_stock] += add_quantity
    else:
        dict_inventory[add_stock] = add_quantity

    return dict_inventory

def remove_inventory(remove_stock,remove_quantity,dict_inventory):
    if remove_stock in dict_inventory:
        if dict_inventory[remove_stock] >= remove_quantity:
            dict_inventory[remove_stock] -= remove_quantity
            return "Removal of stock successful"
        else:
            return "Reject the stock removal"
    else:
        return "Not found"

def view_inventory(dict_inventory):
    print(f"The avaliable stock are :{dict_inventory}")
def main_inventory():
    dict_inventory={}
    while True:
        choice=int(input(" \n 1.Add Stock : \n 2.Remove Stock : \n 3.View Stock \n 4.Exit \n Enter the choice :"))
        match choice:
            case 1:
                add_stock=input("Enter the stock to add :")
                add_quantity=int(input("Enter the quantity of stock :"))
                print(f"{add_inventory(add_stock,add_quantity,dict_inventory)}")


            case 2:
                remove_stock=input("Enter the stock need to remove : ")
                remove_quantity = int(input("Enter the quantity to remove: "))
                print(f"{remove_inventory(remove_stock,remove_quantity,dict_inventory)}")
            case 3:
                view_inventory(dict_inventory)
            case 4:
                print("Exiting.......")
                break
main_inventory()