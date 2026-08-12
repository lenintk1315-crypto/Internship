def aggregate_scanning():
    list_int=[45, 2, 89, 12, 7] 
    greatest=list_int[0]
    smallest=list_int[0]
    for num in list_int:
        if num > greatest:
            greatest=num
        if num < smallest:
            smallest=num
    print(f" Greatest No is :{greatest}\n Smallest No is :{smallest}")
aggregate_scanning()
