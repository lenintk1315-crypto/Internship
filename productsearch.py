def search(product,items):
    #  product=input("Enter the products\n")
    #  for items in product:
     if product in items:
         print("Product is found")
     else:
         print("Product is not found")
    # product=input("Enter the products\n")
items=input("Enter the items\n").split()
product=input("Enter the product\n")
search(product,items)