n = 600851475143 
gpf = 1
start_prime = 2

def find_first_divisor(n,start):
    while start<=n/2:
        if n%start==0:
            return start
        if start==2:
            start +=1
        else:
            start +=2
    return n

def remove_factor(n,factor):
    while n%factor == 0:
        n = n/factor
    return n

def find_greatest_prime_divisor(n):
    gpf = 1
    start_prime = 2
    list_factors = []
    while n>1:
        divisor = find_first_divisor(n,start_prime)
        if divisor > gpf:
            gpf = divisor
        n = remove_factor(n,divisor)
    return gpf

print find_greatest_prime_divisor(600851475143)



