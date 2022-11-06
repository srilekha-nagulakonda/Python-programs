#first type
c=input("enter character:")
if c=='A' or c=='a' or c=='E' or c=='e' or c=='I' or c=='i' or c=='O' or c=='o' or c=='U' or c=='u' :
    print("It is a vowel character")
else:
    print("It is a consonat")


#second type
if c in ['a','e','i','o','u']:
    print("It is a vowel character")
else:
    print("It is a consonat")




#largest among three numbers

a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a >= b and a >= c:
    print("A is the greatest value")
elif  b >= c and b >= c:
    print("B is the greatest value")
else:
    print("C is the greatest value")

