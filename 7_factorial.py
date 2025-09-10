def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

num = int(input("Enter number: "))
print(f"Factorial of {num} is: {fact(num)}")
