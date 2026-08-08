def tracking_loop():
    sum=0
    for current_number in range(0,10):
        if current_number==0:
             previous_number=0 
        else:
             previous_number=current_number -1   
        sum=sum+current_number
        print(f" previous Number :{previous_number} \n current Number :{current_number}\n Sum :{sum}")
tracking_loop()



