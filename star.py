# Get the height of the pyramid
n = int(input("Height: "))

# Loop through each row
for row in range(1, n + 1):
    # Print spaces before hashes to center the pyramid
    for space in range(n - row, 0, -1):
        print(" ", end="")

    # Print hashes (forward loop)
    for hash_count in range(1, 2*row):
        print("#", end="")

    # Move to the next line
    print()
