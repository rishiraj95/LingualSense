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
    T = int(input("Enter number of test cases: "))
    
    for _ in range(T):
        # Read N, X, Y for the current test case
        N, X, Y = map(int, input("Enter number of items, discount cost, discount offer: ").split())
        # Read the list of prices for the current test case
        A = list(map(int, input(f"Enter {N} item prices: ").split()))

        print(coup(N, X, Y, A))

# Run the program
if __name__ == "__main__":
    main()
