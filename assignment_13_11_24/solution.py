def can_reduce_to_one_element(N, K, A):
    # Case when there's only one element
    if N == 1:
        return "YES"
    
    # Sort the array to check the two smallest elements
    A.sort()
    
    # Check the sum of the two smallest elements
    if A[0] + A[1] <= K:
        return "YES"
    else:
        return "NO"


result = []  # Empty list for storing output
T = int(input())  # Number of test cases
    
for _ in range(T):
    N, K = map(int, input().split())  # Read N and K
    A = list(map(int, input().split()))  # Read the array
        
    # Process each test case are stored in the result list
    result.append(can_reduce_to_one_element(N, K, A))
    
print("\n".join(result))