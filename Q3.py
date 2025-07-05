# Question 3: Loops and Summation
# 1. Prompts the user to enter a positive number n.
n = int(input("Enter a number: "))

# Initialize sum for even numbers
sum_of_even_numbers = 0

# 2. Uses a loop to calculate and display the sum of all even numbers from 1 to n.
for i in range(1, n + 1):
    if i % 2 == 0:  # Check if the number is even
        sum_of_even_numbers += i

print(f"Sum of even numbers: {sum_of_even_numbers}")