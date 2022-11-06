n=input("enter binary data:")
print(n)
l=list(n)
l.reverse()
print(l)
sum = 0
for i in range(len(l)):
  sum= sum + int(l[i])*pow(2,i)
print(sum)