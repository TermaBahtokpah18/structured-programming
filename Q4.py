 # Question 4: Functions

# 1. Define a function called is_prime(n) that checks if a given number n is a prime number.
# 2. Returns True if prime, False otherwise.
def is_prime(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(n**0.5) + 1): # Check for divisibility from 2 up to the square root of n
        if n % i == 0:
            return False  # If divisible, it's not prime
    return True  # If no divisors found, it's prime

# Then:
# 1. Ask the user for a number.
number = int(input("Enter a number: "))

# 2. Call the function and display a message saying whether the number is prime.
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")