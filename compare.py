a=int(input("A:"))
b=int(input("B:"))
c=int(input("C:"))
if((a>=b)and(a>=c)):
     print("A is larger than B and C")
elif((b>=a)and(b>=c)):
    print("B is larger than A and C")
else:
     print("C is larger than A and B")