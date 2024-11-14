test_cases =int(input())
responses =[]

for _ in range(test_cases):
    N, X, Y = map(int, input().split())
    prices = list(map(int, input().split()))
    
    total_original = sum(prices)
    total_discounted = sum(max(price - Y, 0) for price in prices) + X

    if total_discounted < total_original:
        responses.append("COUPON")
    else:
        responses.append("NO COUPON")

print("\n".join(responses)) 
