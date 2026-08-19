def file_workflow():
    with open("sample.txt","r") as file:
        content=file.read()
        counting=content.split()
        count=len(counting)
        print(f"The count is :{count} ")
file_workflow()