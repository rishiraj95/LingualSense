<<<<<<< HEAD
t = int(input())
for p in range(t):

    # Read Input
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))


    # Calculate the Original and Discounted Price
    original = 0
    discounted = x # The Cost of Coupon Added
    for i in range(n):
        original += a[i] # The Original Price Added with Value of Every Item if bought without Coupon
        if y < a[i]: # CHECK: If the Discount Price is less than the Original Price otherwise no need to Add Zero
            discounted += a[i] - y


    if discounted < original: 
        print("COUPON") # If the Discounted Price (on use of Coupon) is Less than the Original Price
    else:
        print("NO COUPON") # If Coupon is Not Useful and Original Price is Less than the Discounted Price after using Coupon
=======
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
>>>>>>> 4ed14ad3d1df1bdfe806c5cdf449d5129b65bedb
