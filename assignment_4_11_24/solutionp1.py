# Function to determine whether Chef should buy the coupon
def should_buy_coupon(N, X, Y, prices):
    # Calculate total cost without coupon
    total_without_coupon = sum(prices)
    
    # Calculate total cost with coupon
    total_with_coupon = X  # Start with the cost of the coupon itself
    for price in prices:
        if price <= Y:
            total_with_coupon += 0  # Item becomes free
        else:
            total_with_coupon += (price - Y)  # Discounted price
    
    # Decision
    if total_with_coupon < total_without_coupon:
        return "COUPON"
    else:
        return "NO COUPON"

# Reading number of test cases
T = int(input("Enter number of test cases: "))

# Processing each test case
results = []
for _ in range(T):
    # Read N, X, Y
    N, X, Y = map(int, input("Enter N, X, Y: ").split())
    # Read the prices of items
    prices = list(map(int, input("Enter item prices: ").split()))
    
    # Determine if Chef should buy the coupon and store the result
    results.append(should_buy_coupon(N, X, Y, prices))

# Output all results
print("\n".join(results))
