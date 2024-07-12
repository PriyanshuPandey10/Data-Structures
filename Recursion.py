#Program to find the sum of first n natural numbers using recursion

def f1(n):
    if n==1:
        return 1
    sum=n+f1(n-1)
    return sum
r=f1(5)
print(r)
