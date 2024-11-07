# A=[10,20,30,15,24]
# c1=c2=0
# def coupon(x,y):
#     c1=x
#     for i in A:
#         if A[i]<=y:
#             c1=c1+0
#         else:
#             c1=c1+A[i]-y
# def without():
#     for i in A:
#         c2=c2+A[i]
# coupon(50,12)
# without()
# if c1<c2:
#     print("coupon")
# else:
#     print("No coupon")

# A = [10, 20, 30, 15, 24]


# def input_list():
#     userinput = input("Enter the list of numbers (space-separated): ")
#     A = list(map(int, userinput.split()))
#     return A
# c1 = c2 = 0

# def coupon(x, y):
#     global c1 
#     for price in A: 
#         if price <= y:
#             c1 += 0  # No discount applied, so nothing changes
#         else:
#             c1 += price - y  # Apply the discount and add to c1

# def without():
#     global c2  
#     for price in A:  # Iterate through the elements in A
#         c2 += price  # Add the full price to c2

# # Example test case:
# coupon(50, 12)  # Apply the coupon logic with a threshold of 12
# without()  # Calculate the total without the coupon

# # Compare the totals and print the result
# if c1 < c2:
#     print("coupon")
# else:
#     print("No coupon")


    ## for testcases
def coup(N, X, Y, A):
    ttl_wout_coupon = sum(A)

    ttl_w_coupon = X  
    for price in A:
        if price <= Y:
            ttl_w_coupon += 0 
        else:
            ttl_w_coupon += (price - Y)  
    
    if ttl_w_coupon < ttl_wout_coupon:
        return "COUPON"
    else:
        return "NO COUPON"

# Main function to handle multiple test cases
def main():
    # Read number of test cases
    T = int(input("Enter no of test cases"))
    
    for _ in range(T):
        # Read N, X, Y for the current test case
        N, X, Y = map(int, input("Enter number of items, discountcost,discountoffer").split())
        # Read the list of prices for the current test case
        A = list(map(int, input("Enter " + str(N) + " items: ").split()))

        print(coup(N, X, Y, A))

# Run the program
if __name__ == "__main__":
    main()


# No of test caases:2

# Test case 1
# No.of Iems, Discountcost, Discountoffer:5 10 3
# Items:5 7 8 4 6

# Test case 2
# No.of Iems, Discountcost, Discountoffer:3 5 6
# Items:10 11 12
