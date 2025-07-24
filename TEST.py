# Bus Ticket Booking System
# Author: [Your Name]
# Date: [Today's Date]

# Function to calculate total cost with possible discount
def calculate_cost(seats):
    price_per_seat = 20000
    total_cost = seats * price_per_seat
    discount = 0

    # Apply 10% discount for booking 4 or 5 seats
    if seats >= 4:
        discount = 0.10 * total_cost
        total_cost -= discount

    return total_cost, discount

# Initialize total available seats
available_seats = 30

# Booking loop
while available_seats > 0:
    print(f"\nAvailable seats: {available_seats}")
    try:
        seats_requested = int(input("Enter number of seats to book (1-5): "))
        
        # Validate input
        if seats_requested < 1 or seats_requested > 5:
            print("Invalid entry. You can only book between 1 and 5 seats.")
            continue

        if seats_requested > available_seats:
            print(f"Booking refused. Only {available_seats} seats remaining.")
            continue

        # Calculate cost and apply discount if needed
        total_cost, discount = calculate_cost(seats_requested)

        if discount > 0:
            print(f"Discount applied: {int(discount)} UGX")

        print(f"Amount to pay: {int(total_cost)} UGX")
