###
"""
    problem statement:
    Determine whether Chef should buy the discount coupon or not.

    N (int): Number of items in the shop.
    X (int): Cost of the discount coupon.
    Y (int): Discount amount for each item.
    prices (list): List of prices for each item.

    Returns:
    str: "COUPON" if the discount coupon should be bought, "NO COUPON" otherwise.
"""
def take_discount_or_not(N, X, Y, prices):

    # Calculate the total cost without the discount coupon by summing all item prices
    total_without_coupon = sum(prices)

    # Initialize the total cost with the discount coupon
    # Start with the price of the discount coupon itself
    total_with_coupon = X

    # Loop over each item price to calculate the discounted total cost
    for price in prices:
        # If the item's price is less than or equal to the discount amount (Y), no discount is applied
        if price <= Y:
            total_with_coupon += 0  # No reduction in price for items that cost less than or equal to Y
        else:
            # Apply the discount to the price of items that cost more than Y
            total_with_coupon += price - Y

    # Compare the total cost with and without the coupon to decide whether to buy it
    if total_with_coupon < total_without_coupon:
        # If the discounted total cost is lower, return "COUPON"
        return "COUPON"
    else:
        # Otherwise, return "NO COUPON"
        return "NO COUPON"

# Example usage
t = int(input("Enter the number of test cases: "))

# Loop through each test case
for i in range(t):
    print(f"\nTest Case {i + 1}:")  # Print test case number
    try:
        # Read and convert N, X, Y values from input (space-separated)
        N, X, Y = map(int, input("Enter N, X, Y (space-separated): ").split())
    except ValueError:
        # Handle invalid input where the user does not enter exactly three integers
        print("Invalid input. Please enter three numbers separated by spaces.")
        continue

    # Read the item prices as a list of integers from input (space-separated)
    prices = list(map(int, input("Enter item prices (space-separated): ").split()))
    
    # Call the function to decide whether to buy the coupon or not and store the result
    result = take_discount_or_not(N, X, Y, prices)
    
    # Print the result clearly for the current test case
    print("Result:", result)  # Print the result clearly

