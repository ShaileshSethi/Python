# Simple calculator program

a= int(input("Enter first number: "))
b= input("Enter operator: ")
c= int(input("Enter second number: "))
if b == "+":
    print(a+c)
elif b == "-":
    print(a-c)
elif b == "*":
    print(a*c)
elif b == "/":
    print(a/c)

