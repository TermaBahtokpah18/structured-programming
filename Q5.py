# Question 5: List Processing
# 1. Allows the user to enter 5 numbers, storing them in a list.
numbers = []
print("Enter 5 numbers:")
for i in range(5):
    num = float(input()) # Using float to allow for decimal numbers if needed, though example shows integers
    numbers.append(num)

# 2. Displays:
# a) The list of numbers
print(f"Numbers: {numbers}")

# b) The maximum, minimum, and average
maximum = max(numbers)
minimum = min(numbers)
average = sum(numbers) / len(numbers)

print(f"Maximum: {int(maximum)}" if maximum == int(maximum) else f"Maximum: {maximum}") # Display as int if whole number
print(f"Minimum: {int(minimum)}" if minimum == int(minimum) else f"Minimum: {minimum}") # Display as int if whole number
print(f"Average: {average}")

# c) The list in sorted order
sorted_numbers = sorted(numbers)
# Convert sorted numbers to integers if they were originally whole numbers for display consistency
sorted_numbers_for_display = [int(num) if num == int(num) else num for num in sorted_numbers]
print(f"Sorted: {sorted_numbers_for_display}")
