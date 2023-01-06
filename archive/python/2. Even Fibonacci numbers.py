def fibonacci_nums_sum_under_n(n: int):
  """
  fibonacci_nums_sum_under_n sums the fibonnaci numbers up to the given int n input
  n: integer
  """
  n1 = 0                              #fibonacci number 1
  n2 = 1                              #fibonacci number 2
  fib_nums = []                       #fibonacci number list
  fib_nums_even = []                  #fibonacci number list containing only evens
  if n == 0:                          #in case n = 0
    return('n must be > 0')
  elif n == 1:                        #in case n = 1
    fib_nums.append(n1)
  else:
    while n2 < n:                     #generate fibonacci numbers
      fib_nums.append(n2)
      nth = n1 + n2                   #nth fibonacci number by summing fibonacci number 1 + 2 
      n1 = n2
      n2 = nth
    for num in fib_nums:              #add only the even fibonacci numbers to appropriate list
      if num % 2 != 0:
        fib_nums_even.append(num)
  return sum(fib_nums_even)

#Function input
n = 4000000        
print(fibonacci_nums_sum_under_n(n))
