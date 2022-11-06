year=int(input("enter year:"))
if year%400==0 and year%100==0:
    print("leap year")
elif year%4==0 and year%100 != 0:
     print("leap year")
else: 
    print("not a leap year")


#positive number or not
n=int(input("enter number:"))
if n>0:
    print("positive number")
elif n==0:
    print("zero")
else:
    print("negative number")
