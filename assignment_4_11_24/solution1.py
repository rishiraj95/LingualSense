<<<<<<< HEAD
<<<<<<< HEAD
## Write your program here
# Taking user's input
N = int(input("Enter number of items in the shop: "))
X = int(input("Enter cost of coupon: "))
Y = int(input("Enter the discount per item: "))

#reading list of items
prices = list(map(int, input("Enter prices of the items: ").split()))  

# calculate total cost without discount
total_cost_without_coupon = sum(prices)


# Calculate total cost with the coupon
total_cost_with_coupon = X  # Start with the coupon cost

# Apply the discount Y to each item 
for price in prices:
    if price > Y:
        total_cost_with_coupon += (price - Y)
    else:
        total_cost_with_coupon += 0  # Item is free if price <= Y

# Determine if Chef should buy the coupon
if total_cost_with_coupon < total_cost_without_coupon:
    print("COUPON")
else:
    print("NO COUPON")
=======

>>>>>>> fcebccd3f0a3aa3fe12928b0376ad16eb4dfcf42
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
