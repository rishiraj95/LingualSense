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