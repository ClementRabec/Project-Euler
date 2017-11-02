number = 2520
found = False

while not found:
  if number % 4 == 0 and number % 7 == 0 and number % 8 == 0 and number % 9 == 0 and number % 11 == 0 and number % 12 == 0 and number % 13 == 0 and number % 14 == 0 and number % 16 == 0 and number % 17 == 0 and number % 18 == 0 and number % 19 == 0:
    break
  
  number += 2520
  
print (number)
