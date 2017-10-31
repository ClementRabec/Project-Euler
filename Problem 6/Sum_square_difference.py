sum_of_the_squared = 0
square_of_the_sum = 0
i=1

while i <= 100:
  sum_of_the_squared += i ** 2
  square_of_the_sum += i
  i += 1
  square_of_the_sum
  
print square_of_the_sum ** 2 - sum_of_the_squared
