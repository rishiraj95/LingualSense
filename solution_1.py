def Check_coupon(n,x,y,A):
    priceWithOut = sum(A)
    reducedA = [(A[i] - y) if y < A[i] else 0 for i in range(len(A))]

    priceWith = sum(reducedA)
    totalPrice = priceWith + x
    if totalPrice >= priceWithOut:
        return "No Coupon"
    else:
        return "Coupon"

T = int(input())
N , X , Y = map(int,input().split())
A = list(map(int,input().split()))
for i in range(T):
    print(Check_coupon(N,X,Y,A))

     