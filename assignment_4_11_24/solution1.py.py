def should_buy_coupon(N, X, Y, prices):
    
    total_without_coupon = sum(prices)
    
    
    total_with_coupon = sum(max(0, price - Y) for price in prices) + X
    
    if(total_with_coupon<total_without_coupon):
        return "COUPON"
    
    else:
        return "NO COUPON"
    
    return "COUPON" if total_with_coupon < total_without_coupon else "NO COUPON"


T = int(input("Enter the number of test cases: "))
results = []

for _ in range(T):

    NN, XX, YY = map(int, input("Enter N, X, Y: ").split())
    prices = list(map(int, input("Enter the prices: ").split()))

    results.append(should_buy_coupon(NN, XX, YY, prices))

print("\n".join(results))
