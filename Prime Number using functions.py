 def prime(n):
 for i in range(2,n):
    if n%i==0:
     return 0
    else:
       return 1
  n=int(input("Enter a number: "))
  print(prime(n))
