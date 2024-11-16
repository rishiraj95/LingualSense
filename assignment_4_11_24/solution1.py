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
