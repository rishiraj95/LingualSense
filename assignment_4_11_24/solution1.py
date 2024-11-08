def should_buy_coupon(T, test_cases):
    results = []
    for case in test_cases:
        N, X, Y = case[0]
        prices = case[1]
        
        # Calculate total without coupon
        total_without_coupon = sum(prices)
        
        # Calculate total with coupon
        total_with_coupon = sum(max(0, price - Y) for price in prices) + X
        
        # Compare and decide
        if total_with_coupon < total_without_coupon:
            results.append("COUPON")
        else:
            results.append("NO COUPON")
    
    return results

# Example usage:
T = 5
test_cases = [
    ((4, 30, 10), [15, 8, 22, 6]),
    ((4, 40, 10), [15, 8, 22, 6]),
    ((4, 34, 10), [15, 8, 22, 6]),
    ((2, 10, 100), [60, 80]),
    ((3, 30, 5), [50, 60, 50])
]

output = should_buy_coupon(T, test_cases)
for result in output:
    print(result)
