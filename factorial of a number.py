#type1 
n=int(input("enter a number:"))
fact=1
if n==0 or n==1:
    print("the factorial is value is ", fact)
else:
    for i in range(1,n+1):
        fact=fact*i
    print("factorial value is ",fact)



#type2
d=int(input("enter a number: "))

def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
f=factorial(d)
print(f)