def write_file():
    with open("sample.txt","w") as file:
        file.write("Monday....\n")
        file.write("Tuesday...\n")
        file.write("Wednesday....\n")

def read_file():
    with open("sample.txt","r") as file:
        content=file.read()
        print(content)
write_file()
read_file()