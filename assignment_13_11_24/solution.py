def can_reduce_to_one_element(N, K, A):
    
    # Sort the array to check the two smallest elements
    A.sort()
    
    # Case when there's only one element
    if N == 1:
        return True

    # Iterate through the array, checking if we can find a pair of elements that sum to at most K
    for i in range(len(A) - 1):
        if A[i] + A[i + 1] <= K:
            return True

    return False


result = []  # Empty list for storing output
T = int(input())  # Number of test cases
    
for _ in range(T):
    N, K = map(int, input().split())  # Read N and K
    A = list(map(int, input().split()))  # Read the array
    
    # Process to check for the function is True or Flase and store the result in the list
    if can_reduce_to_one_element(N, K, A):
        result.append("YES")
    else:
        result.append("NO")
    
print("\n".join(result))