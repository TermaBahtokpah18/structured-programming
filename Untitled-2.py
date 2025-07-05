# Question 2: Conditional Statements

# 1. Prompts the user to input a numeric score.
score = float(input("Enter a numeric score: "))

# 2. Determines the grade using the grading scale and 3. Prints the corresponding grade.
if 80 <= score <= 100:
    print("Grade: A")
elif 70 <= score <= 79:
    print("Grade: B")
elif 60 <= score <= 69:
    print("Grade: C")
elif 50 <= score <= 59:
    print("Grade: D")
else: # Below 50
    print("Grade: F")