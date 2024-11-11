def should_buy_coupon(N, X, Y, prices):
    total_without_coupon = sum(prices)
    total_with_coupon = sum(max(price - Y, 0) for price in prices) + X
    return "COUPON" if total_with_coupon < total_without_coupon else "NO COUPON"

N = int(input("Enter the number of items (N): "))
X = int(input("Enter the coupon cost (X): "))
Y = int(input("Enter the discount per item (Y): "))
prices = list(map(int, input("Enter the prices of items separated by spaces: ").split()))

print(should_buy_coupon(N, X, Y, prices))
