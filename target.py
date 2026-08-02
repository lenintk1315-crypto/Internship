def targett():
    num=[3,5,7,9,11,15]
    target=10
    for x in range(len(num)):
         for j in range(x+1,len(num)):
           if num[x]+num[j]==target:
              print("target found",num[x],"+",num[j],"=",target)
           else:
               print("target not found")
targett()