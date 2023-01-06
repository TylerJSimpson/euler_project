#3. Largest prime factor

def largest_prime_factor(num: int):
    
    #create variables
    n = 2
    factors = []
    #account for num 1
    if num == 1:
        return 1
    #add prime factors to factors list
    while n ** 2 <= num:
        if num % n == 0:
            factors.append(n)
            num //= n
        else:
            n += 1
    if num > 1:
       factors.append(num)
    #return the highest prime factor
    return max(factors)

n = 600851475143
print(largest_prime_factor(n))
