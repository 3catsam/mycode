def is_prime(x):
    if x==2:
        return True
    elif x<2:
        return False
    else:
        k=0
        for n in range(2,x):
            if x%n==0:
                k+=1
        if k>=1:
            return False
        else:
            return True
for i in range(100):
    if is_prime(i) is True:
        print i,
