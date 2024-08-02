print("---------MINI CALCULATOR---------")
num1=float(input("Enter First Number"))
num2=float(input("Enter Second Number"))

print("Press 1 for Addition \n Press 2 for Substraction \n Press 3 for Multiplication \n Press 4 for Division")
choice=int(input("Enter your Choice"))
if choice==1:
    print(f"Sum of {num1} and {num2} = {num1+num2}")
elif choice==2:
    print(f"Sub of {num1} and {num2} = {num1-num2}")
elif choice==3:
    print(f"Multiplication of {num1} and {num2} = {num1*num2}")
elif choice==4:
    print(f"Division of {num1} and {num2} = {num1/num2}")
else:
    print("Invalid Input")

