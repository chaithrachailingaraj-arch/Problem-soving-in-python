numbers = [1, 2, 4, 5, 6]

# Step 1: Find n (largest number expected)
n = max(numbers)

# Step 2: Formula for sum of first n natural numbers
S = n * (n + 1) // 2

# Step 3: Calculate the total sum of the list
Total = 0
for number in numbers:
    Total += number

# Step 4: Compare and find the missing number
if S != Total:
    print("Number missing")
    print("Missed number is:", S - Total)
else:
    print("Number not missing")
