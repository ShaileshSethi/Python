# Ask how many numbers to input
n = int(input("How many numbers do you want to average? "))

# Initialize sum to 0
total = 0

# Loop to take 'n' inputs
for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    total += num

# Calculate average
average = total / n

# Print result
print("The average is:", average)
