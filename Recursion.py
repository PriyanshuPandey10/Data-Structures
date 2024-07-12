#Program to find the sum of first n natural numbers using recursion

# def f1(n):
#     if n==1:
#         return 1
#     sum=n+f1(n-1)
#     return sum
# r=f1(5)
# print(r)

#Program to print first N natural numbers
# def printN(num):
#     if num>0:
#         printN(num-1)
#         print(num)
# naturalnumber=printN(5)

#Program to print first N natural numbers in recursive order
# def printNreverse(num):
#     if num>0:
#         print(num)
#         printNreverse(num-1)
# naturalnumber=printNreverse(5)

#Program to print first n odd natural numbers
def noddnatural(n):
    if (n>0 ):
        noddnatural(n-1)
        if n%2!=0:
            print(n)
        
noddnatural(20)
