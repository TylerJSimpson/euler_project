#3. Largest prime factor

def largest_prime_factor(num: int):
    """
    largest_prime_factor sums the fibonnaci numbers up to the given int n input
    num: integer
    """   
    n = 2                                   #set counter n = 2
    factors = []                            #create list to hold factors
    if num == 1:                            #account for num = 1
        return 1
    while n ** 2 <= num:                    #use square root of n to quickly remove options above largest prime factor
        if num % n == 0:
            factors.append(n)
            num //= n
        else:
            n += 1
    if num > 1:
       factors.append(num)                  #append prime factors
    return max(factors)                     #return max prime factor

n = 600851475143
print(largest_prime_factor(n))
