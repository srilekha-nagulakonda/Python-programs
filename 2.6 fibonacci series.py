n1,n2=0,1
nterms=int(input("enter how many number of terms you want:"))
count=0
if nterms <= 0:
  print("enter positive number.")
elif nterms==1:
  print(n1)
else:
  print("The sequence is :")
  while count<nterms:
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    count+=1