def computegcd(a,b):
  if b==0:
    return a
  else:
    return computegcd(b,a%b)
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
print(computegcd(n1,n2))