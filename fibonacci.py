num=int(input("enter a number"))
a=0
b=1
print("fibonacci series")
for i in range(num):
    print(a,end=" ")
    temp=a
    a=b
    b=temp+b