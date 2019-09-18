a=[]
n=int(input("Enter the limit:"))
print("Enter the elements:")
for i in range(n):
    a.append(input(""))
print("\nThe list is:",a,"\nThe tuple is:",tuple(a),"\nThe set is:",set(a))
