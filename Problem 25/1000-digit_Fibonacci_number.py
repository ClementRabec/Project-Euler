Fn1 = 1
Fn2 = 1
length = 0
index = 2
digits = 1000

while length < digits:
  Fn = Fn1 +Fn2
  Fn2 = Fn1
  Fn1 = Fn
  length = len(str(Fn))
  index += 1
  
print index
