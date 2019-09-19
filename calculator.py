import module
a=int(input("A="))
b=int(input("B="))
ch=1
while(ch==1):
    op=int(input("Enter the operation\n1.Addition\n2.Subtraction\n3.m\Multiplication\n4.Division:\n"))
    if(op==1):
        module.add(a,b)
    elif(op==2):
        module.Sub(a,b)
    elif(op==3):
        module.mul(a,b)
    elif(op==4):
        module.div(a,b)
    else:
        print("Invalid Operation!!!")
    ch=int(input("Do you want to continue?(Yes/1,No/0):"))
