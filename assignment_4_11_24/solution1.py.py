###
def should_buy_coupon(n, x, y, prices):
    total_without_coupon = sum(prices)
    
    # Calculate the total cost with coupon
    total_with_coupon = sum(max(0, price - y) for price in prices) + x
    
    # Check if buying the coupon is beneficial
    return "COUPON" if total_with_coupon < total_without_coupon else "NO COUPON"

# Read input
t = int(input().strip())
results = []
for _ in range(t):
    # Read values for each test case
    n, x, y = map(int, input().strip().split())
    prices = list(map(int, input().strip().split()))
    
    # Compute result for this test case
    result = should_buy_coupon(n, x, y, prices)
    results.append(result)

# Output all results
print("\n".join(results))
