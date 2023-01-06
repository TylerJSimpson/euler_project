def sum_multiples_of_5_and_3(n: int):
    """
    sum_multiples_of_5_and_3 takes int n and sums the multiples of 3 and 5
    n: integer
    """
    multiples_of_5 = []                                     #adds multiples of 5 of n to list
    for num in range(1,n):
        if num % 5 == 0:
            multiples_of_5.append(num)
    multiples_of_3 = []                                     #adds multiples of 3 of n to list
    for num in range(1,n):
        if num % 3 == 0:
            multiples_of_3.append(num)
    all_multiples = multiples_of_5 + multiples_of_3         #combines multiples of 5 and 3 of n 
    final_multiples = []
    [final_multiples.append(x)                              #creates a new list without duplicates
     for x in all_multiples if x not in final_multiples]
    return sum(final_multiples)                             #returns sum of all multiples of 5 and 3 of n
    

#Function input
n = 1000
print(sum_multiples_of_5_and_3(n))
