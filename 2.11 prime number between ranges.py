lower=int(input("enter lower number:"))
upper=int(input("enter upper number:"))
print("prime numbers between",lower,"and",upper,":")
for i in range(lower,upper+1):
  if i>1:
    for j in range(2,i):
      if i%j==0:
        break
    else:
      print(i)