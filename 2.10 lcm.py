def compute(n1,n2):
  if n1>n2:
    higher = n1
  else:
    higher = n2
  value=higher
  while True:
    if higher%n1==0 and higher%n2==0:
      print("LCM of two numbers value is:",higher)
      break
    else:
      higher+= value

n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
compute(n1,n2)