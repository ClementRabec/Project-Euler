x = 1
x1 = 0
F = 0
sum = 0
while F < 4000000:
  F = x + x1
  x1 = x
  x = F
  if F % 2 == 0:
    sum += F

print sum
