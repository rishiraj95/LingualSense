def can_reduce_to_one_element(n, k, arr):
    # If there's only one element, it's already reduced to one element
    if n == 1:
        return "YES"
    
    # Find the two smallest elements in the array
    arr.sort()
    smallest_sum = arr[0] + arr[1]
    
    # Check if their sum is <= K
    if smallest_sum <= k:
        return "YES"
    else:
        return "NO"

# Reading input
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(can_reduce_to_one_element(n, k, arr))
