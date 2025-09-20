# pattern_drawing.py

# Prompt the user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to handle rows
while row < size:
    # Use a for loop to handle columns in each row
    for col in range(size):
        print("*", end="")  # print * without new line
    print()  # move to next line after each row
    row += 1
