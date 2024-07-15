Program to find the sum of first n natural numbers using recursion

def f1(n):
    if n==1:
        return 1
    sum=n+f1(n-1)
    return sum
r=f1(5)
print(r)

Program to print first N natural numbers
def printN(num):
    if num>0:
        printN(num-1)
        print(num)
naturalnumber=printN(5)

Program to print first N natural numbers in recursive order
def printNreverse(num):
    if num>0:
        print(num)
        printNreverse(num-1)
naturalnumber=printNreverse(5)

Program to print first n odd natural numbers
def noddnatural(n):
    if (n>0 ):
        noddnatural(n-1)
        if n%2!=0:
            print(n)
        
noddnatural(20)

Program to print first n even natural numbers
def nevennatural(n):
    if (n>0 ):
        nevennatural(n-1)
        if n%2==0:
            print(n)
        
nevennatural(20)


Program to print first n odd natural numbers in reverse order
def oddreverse(n):
    if n>0:
        print(2*n-1,end=' ')
        oddreverse(n-1)
oddreverse(20)


Program to print first n odd natural numbers in reverse order
def evenreverse(n):
    if n>0:
        print(2*n,end=' ')
        evenreverse(n-1)
evenreverse(20)

Program to print sum of  first n odd natural numbers
def odd(n):
    if n==1:
        return 1
    return 2*n-1+odd(n-1)
print("Sum is ",odd(10))
    
Program to print sum of  first n even natural numbers
def even(n):
    if n==1:
        return 2
    return 2*n+even(n-1)
print("Sum is ",even(10))

Program to find the factorial of a number using recursion
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print("Factorial is",fact(5))

Program to find sum of squares of n natural numbers
def sq(n):
    if n==1:
        return 1
    return n*n +sq(n-1)
print("Sum of squares is",sq(5))