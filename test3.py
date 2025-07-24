def calculate_fine(days_late):
    if days_late <= 0:
        return 0, False
    elif days_late <= 7:
        return days_late * 1000, False
    elif days_late < 30:
        return days_late * 2000, False
    else:
        return 50000, True

try:
    days = int(input("Enter number of days late: "))
    if days < 0:
        print("Invalid input. Days cannot be negative.")
    else:
        fine, banned = calculate_fine(days)
        print("\nSummary:")
        print(f"Days late: {days}")
        print(f"Fine: {fine} UGX")
        print(f"Banned: {'Yes' if banned else 'No'}")

except ValueError:
    print("Invalid input. Please enter a valid number.")
