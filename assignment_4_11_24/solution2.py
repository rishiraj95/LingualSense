<<<<<<< HEAD
t = int(input())
for _ in range(t):

    # Read Input
    n = int(input())
    a = list(map(int, input().split()))
    
    # Calculate the Minimum Value and Count the Number of Minimum Values
    count = 1 # There will be Atleast One Minimum Value Always
    min_val = a[0] # Initialize the Minimum Value with First Element
    for i in range(1, n):
        if a[i] < min_val:
            min_val = a[i] # Update the Minimum Value
            count = 1 # Reset the Count as we have founf the new Minimum Value and thus Total Count will be 1 now
        elif a[i] == min_val:
            count += 1 # Increment the Count if the Current Value is Equal to the Minimum Value
    
    if n < 2:
        print(0) # There is Only one Element in the List
    else:
        print(n - count) # The Number of Elements to be Changed will be the Total Number of Elements - Count of Minimum Values
=======
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
>>>>>>> 4ed14ad3d1df1bdfe806c5cdf449d5129b65bedb
