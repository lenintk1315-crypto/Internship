# def count_down_timer():
#     timer=int(input("Enter the countdown :"))
#     for timer in range(timer,-1,-1):
#         print(timer)
#     print("blast off.....")
# count_down_timer()


def tracking_loop():
    num=int(input("enter the  timer :"))
    import time
    for num in range(num,-1,-1):
          time.sleep(1)
          print(num)
    print("blast off....")
tracking_loop()






# step countdown=-1(negative or positive count upto condition)