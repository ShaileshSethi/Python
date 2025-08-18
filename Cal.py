print("Welcome to the simple calculator!")
# Simple calculator program 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

c = input("Enter operation + for addition, - for subtraction, * for multiplication, / for division: ")

if c == '+':
    print("The sum is:", a + b) 
elif c == '-':
    print("The difference is:", a - b)
elif c == '*':
    print("The product is:", a * b)
elif c == '/':
    if b != 0:
        print("The quotient is:", a / b)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation!")
