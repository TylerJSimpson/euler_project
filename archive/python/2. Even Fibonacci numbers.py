#2. Even Fibonacci numbers

def fibonacci_nums_sum_under_n(n):

  #set variables
  n1 = 0
  n2 = 1
  fib_nums = []
  fib_nums_even = []

  #generate fibonacci numbers from 1 to n
  if n == 0:
    return('n must be > 0')
  elif n == 1:
    fib_nums.append(n1)
  else:
    while n2 < n:
      fib_nums.append(n2)
      nth = n1 + n2
      n1 = n2
      n2 = nth
    #retain only the even numbers and sum them
    for num in fib_nums:
      if num % 2 != 0:
        fib_nums_even.append(num)
  return sum(fib_nums_even)

n = 4000000        
print(fibonacci_nums_sum_under_n(n))
