def can_reduce_to_one_element(N, K, A):
    # Sort the array to make pairing easier
    A.sort()
    
    # Use two pointers to check pairs from both ends
    left, right = 0, N - 1
    while left < right:
        # Check if the sum of the smallest and largest is within the limit
        if A[left] + A[right] <= K:
            # Remove either element by moving the left pointer up
            left += 1
            right -= 1
        else:
            # If not, only move the right pointer (remove the larger element)
            right -= 1

    # After processing, check if only one element remains
    return left == right

# Read input
T = int(input())
results = []
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    # Check if it's possible to reduce to one element
    if can_reduce_to_one_element(N, K, A):
        results.append("YES")
    else:
        results.append("NO")

# Print results for each test case
print("\n".join(results))
