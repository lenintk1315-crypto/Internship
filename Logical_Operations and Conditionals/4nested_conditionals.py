def triangle(side1,side2,side3):
    def equilateral():
        return side1==side2==side3
    def isosceles():
        return side1==side2 or side2==side3 or side1==side3
    def scalene():
        return side1!=side2!=side3
    if equilateral():
        print("The triangle is an equilateral triangle")
    elif isosceles():
        print("The triangle is an isosceles triangle")
    elif scalene():
        print("The triangle is a scalene triangle")
    else:
        print("The triangle is not valid")
def main():
    side1=int(input("Enter the first side:"))
    side2=int(input("Enter the second side:"))
    side3=int(input("Enter the third side:"))
    triangle(side1,side2,side3)
main()










# /////////////////////////////////////
# def triangle(side1,side2,side3):
#     return side1==side2==side3
# def isosceles(side1,side2,side3):   
#     return side1==side2 or side2==side3 or side1==side3
# def scalene(side1,side2,side3):
#     return side1!=side2!=side3
# def main():
#     side1=int(input("Enter the first side:"))
#     side2=int(input("Enter the second side:"))
#     side3=int(input("Enter the third side:"))
#     if triangle(side1,side2,side3):
#         print("The triangle is an equilateral triangle")
#     elif isosceles(side1,side2,side3):
#         print("The triangle is an isosceles triangle")
#     elif scalene(side1,side2,side3):
#         print("The triangle is a scalene triangle")
#     else:
#         print("The triangle is not valid")
# main()