m = int(input("Enter any number: "))
n = int(input("Enter any second number:"))
for i in range(m, n + 1):
    if (i % 2) != 0:
        i += 1
    else:
        print(i)