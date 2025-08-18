n = int(input("Enter a numeric digit (0-9): "))
if (n == 0):
    print("zero")
elif (n == 1):
    print("one")
elif (n == 2):
    print("two")
elif (n == 3):
    print("three")
elif (n == 4):
    print("four")
elif (n == 5):
    print("five")
elif (n == 6):
    print("six")
elif (n == 7):
    print("seven")
elif (n == 8):
    print("eight")
elif (n == 9):
    print("nine")
elif (n < 0 or n > 9):
    print("Please enter a digit between 0 and 9.")
# ... and so on for other digits
else:
    print("invalid input")