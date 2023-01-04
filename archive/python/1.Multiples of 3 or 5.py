#1.Multiples of 3 or 5

def sum_multiples_of_5_and_3(n):

    #sums multiples of 5 and 3 for n number non-inclusive
    multiples_of_5 = []
    for num in range(1,n):
        if num % 5 == 0:
            multiples_of_5.append(num)
    multiples_of_3 = []
    for num in range(1,n):
        if num % 3 == 0:
            multiples_of_3.append(num)
 
    #removes duplicates nums from lists multiples_of_5 and multiples_of_3 then sums
    all_multiples = multiples_of_5 + multiples_of_3
    final_multiples = []
    [final_multiples.append(x) for x in all_multiples if x not in final_multiples]
    return sum(final_multiples)
    
    
n = 1000
print(sum_multiples_of_5_and_3(n))
