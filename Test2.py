def calculate_total(standard, vegetarian, deluxe):
    total_meals = standard + vegetarian + deluxe
    total_price = standard * 12000 + vegetarian * 10000 + deluxe * 15000
    discount = 0
    if total_meals > 3:
        discount = total_price * 0.10
        total_price -= discount
    return total_meals, discount, total_price

try:
    hour = int(input("Enter current hour (0-23): "))
    if hour < 7 or hour > 19:
        print("Sorry, orders are only accepted between 7:00 AM and 7:00 PM.")
    else:
        print("Welcome to the Campus Cafeteria!")
        print("Menu:")
        print("1. Standard Meal - 12000 UGX")
        print("2. Vegetarian Meal - 10000 UGX")
        print("3. Deluxe Meal - 15000 UGX")

        standard = int(input("Enter number of Standard Meals: "))
        vegetarian = int(input("Enter number of Vegetarian Meals: "))
        deluxe = int(input("Enter number of Deluxe Meals: "))

        if standard < 0 or vegetarian < 0 or deluxe < 0:
            print("Invalid meal count. Must be non-negative.")
        else:
            total_meals, discount, total_price = calculate_total(standard, vegetarian, deluxe)
            print("\nOrder Summary:")
            print(f"Standard Meals: {standard}")
            print(f"Vegetarian Meals: {vegetarian}")
            print(f"Deluxe Meals: {deluxe}")
            print(f"Total meals: {total_meals}")
            print(f"Discount: {int(discount)} UGX")
            print(f"Total to pay: {int(total_price)} UGX")

except ValueError:
    print("Invalid input. Please enter numbers only.")
