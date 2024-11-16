# <<<<<<< HEAD
# Read the size of the array
N = int(input())

# Read the array elements
A = list(map(int, input().split()))

# Find the minimum value in the array
M = min(A)

# Count how many elements are greater than the minimum value
operations = 0
for i in A:
    if i > M:
        operations += 1

# Output the number of operations needed
print(operations)
# =======
def min_to_max_operations(arr):
    """
    Calculates the minimum number of operations to make the minimum value the maximum.

    Args:
        arr: The input array.

    Returns:
        The minimum number of operations.
    """

    min_val = min(arr)
    max_val = max(arr)

    # If the minimum is already the maximum, no operations are needed.
    if min_val == max_val:
        return 0
    # Count elements greater than the minimum value
    operations = 0
    for num in arr:
        if num > min_val:
            operations += 1

    return operations

results = []
T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    results.append(min_to_max_operations(arr))
    
for result in results:
    print(result)
# >>>>>>> 4ed14ad3d1df1bdfe806c5cdf449d5129b65bedb
