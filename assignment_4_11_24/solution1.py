def should_buy_coupon(N, X, Y, prices):
    """
    Determines whether Chef should buy the discount coupon.

    Args:
        N: Number of items.
        X: Cost of the discount coupon.
        Y: Discount amount per item.
        prices: List of prices of the items.

    Returns:
        "COUPON" if Chef should buy the coupon, "NO COUPON" otherwise.
    """

    total_price_without_coupon = sum(prices)
    total_price_with_coupon = X + sum(max(0, price - Y) for price in prices)
    
    if total_price_with_coupon < total_price_without_coupon:
        return "COUPON"
    else:
        return "NO COUPON"

# Empty list for storing the result
result = []
# number of paries
T = int(input())
for _ in range(T):
    N, X, Y = map(int, input().split())
    prices = list(map(int, input().split()))
    result.append(should_buy_coupon(N, X, Y, prices))

print("\n".join(result))
