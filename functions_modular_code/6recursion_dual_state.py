def fibonacci_series(fib):
    if fib==0 or fib==1:
        return fib
    else:
        return fibonacci_series(fib-1)+fibonacci_series(fib-2)
fib=int(input("Enter the limit :"))
result=fibonacci_series(fib)
print(result)