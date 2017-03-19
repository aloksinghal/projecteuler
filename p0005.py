from collections import defaultdict

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
    count = 0
    while n%factor == 0:
        n = n/factor
        count += 1
    return n,count

def find_all_prime_divisors(n):
    factors = defaultdict(int)
    start_prime = 2
    while n>1:
        divisor = find_first_divisor(n,start_prime)
        start_prime = divisor
        n,count = remove_factor(n,divisor)
        factors[divisor] = count
    return factors

def merge_factors(factor_dict1, factor_dict2):
    merged_dict = defaultdict(int)
    for item in factor_dict1.items():
        merged_dict[item[0]] = max(item[1],factor_dict2[item[0]])
    for item in factor_dict2.items():
        merged_dict[item[0]] = max(item[1],factor_dict1[item[0]])
    return merged_dict
        
n=2
result_dict = defaultdict(int)
while n<=20:
    factors = find_all_prime_divisors(n)
    result_dict = merge_factors(result_dict,factors)
    n += 1

result = 1

for key, value in result_dict.items():
    result = result * (key**value)

print result

