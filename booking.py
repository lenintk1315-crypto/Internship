seat=int(input("Enter the number of seats\n"))
def booking(seat):
   book=int(input("Enter the no of seats to be booked\n"))
   if book<=seat:
        seat=seat-book
        print("The seat is booked and the remaining seats are ",seat)
   else:
        print("Seat is not available",)
        print("The seat is not booked and the remaining seats are ",seat)
   return seat
while True:
    choice=input("Book ticket ,yes or No\n")
    if choice=="yes":
      seat=booking(seat)
    else:
        print("Thankyou for using our services")
        break
