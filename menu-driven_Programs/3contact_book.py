def contact_name(cont_name,contacts,cont_no):
    contacts[cont_name]=cont_no
    return contacts

def contact_delete(contacts):
    cont_name = input("Enter the name to delete: ")
    if cont_name in contacts:
        contacts.pop(cont_name)
    return contacts

def contact_search(contacts):
    name = input("Enter the name to search: ")
    if name in contacts:
        print("Name:", name)
        print("Phone:", contacts[name])
    else:
        print("Contact not found")

def contact_list(contacts):
    for name, phone in contacts.items():
        print(f"Name :{name} Phone : {phone}")
            



def contact_main():
    contacts={}
    while True:
        choice=int(input("\n 1.Add Contact : \n 2.Delete Contact : \n 3.Search Contact : \n 4.List Contact : \n 5.Exit .\n Enter the choice :"))
        match choice:
            case 1:
                cont_name=input("Enter the Name :")
                cont_no=int(input("Enter the phone Number :"))
                print(f"The Name is{cont_name} \n The ph No id {cont_no}  {contact_name(cont_name,contacts,cont_no)}")
            case 2:
                    print(f"Name :{cont_name} \n The ph No : {cont_no}  {contact_delete(contacts)}")
            case 3:
                    contact_search(contacts)
            case 4:
                    contact_list(contacts)
            case 5:
                  print("Exiting......")
                  break
contact_main()