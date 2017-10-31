sum = 0
value = 1

while value < 1000:
  if value % 3 == 0 or value % 5 == 0:
    sum += value
  value += 1
print sum
