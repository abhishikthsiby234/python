num=int(input("enter the number:"))
i=1
print(f"Factor  of {num} are:")
while i<=num:
    if num % i == 0:
        print(i,end=" ")
        i+=1