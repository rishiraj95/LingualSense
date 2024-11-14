def can_reduce_to_single_element(n, k, arr):
    # Sort the array 
    arr.sort()

    # Two pointers approach to find pairs
    left, right = 0, n - 1
    while left < right:
        # If the pair satisfies the condition
        if arr[left] + arr[right] <= k:
            # Remove one element from the right side
            right -= 1
        else:
            # If not, remove the largest element
            left += 1

    # If only one element is left, it can be reduced to a single element
    return left == right

# Input reading and handling multiple test cases
t = int(input())
results = []
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if can_reduce_to_single_element(n, k, arr):
        results.append("YES")
    else:
        results.append("NO")

# Output for all test cases
print("\n".join(results))

''' 
# use this formet
3
1 3
1
3 3
2 2 2
4 7
1 4 3 5

YES
YES
YES
'''
