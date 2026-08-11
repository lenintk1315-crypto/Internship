def capitilize_word():
    result=" "
    para=input("Enter the Sentence :")
    for index,value in enumerate(para):  
            if index==0 or para[index - 1]==" ":
                result+=value.upper()
            else:
                 result+=value
    print(result)
capitilize_word()