def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)
nterm=int(input("enter the number of terms:"))
if nterm<=0:
    print("the number is positive")
else:
    print("the number is fibonacci series")
    for i in range(nterm):
        print(fibo(i))


