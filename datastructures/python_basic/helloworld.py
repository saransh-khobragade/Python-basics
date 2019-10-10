def isPrime(num):
  for x in range(1,num//2):
    if(x==1):
      continue
    if(num%x == 0):
      print('not prime')
      isPrime
      return
  #print('prime')

# isPrime(15)
for x in range(2,10):
  #print(x)
  print(str(isPrime(x)))
  

