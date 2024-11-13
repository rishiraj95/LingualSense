def sol():
    T = int(input())  # Read the number of test cases
    results = []

    for _ in range(T):
        N, K = map(int, input().split())  # Read N and K
        A = list(map(int, input().split()))  # Read the array A
        
        if N == 1:
            results.append("YES")
            continue
        
        # Sort the array
        A.sort()

        # Check if the sum of the smallest and largest elements is <= K
        if A[0] + A[-1] <= K:
            results.append("YES")
        else:
            results.append("NO")

    # Print all the results
    for result in results:
        print(result)

# Call the function
sol()

## instead of checking all the elements here it uses a greedy approach that is choosing largest and smallest
