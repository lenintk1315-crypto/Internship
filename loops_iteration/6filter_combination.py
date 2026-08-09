def prime_condition():
    count=0
    for num in range(2,21):
        is_prime=True
        for i in range(2,num):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
             count=count+1

             if count%2==1:
                print(num)
prime_condition()