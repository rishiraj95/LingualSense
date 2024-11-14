def min_operations_to_max(t, test_cases):
    results = []
    for _ in range(t):
        n = test_cases[_][0]
        array = test_cases[_][1]
        
        min_val = min(array)
        max_val = max(array)
        
        
        if min_val == max_val:
            results.append(0)
            continue
        
        array.sort()
        
        operations = 0
        for i in range(len(array)):
            if array[i] != min_val:
                operations += 1
                array[i] = min_val
        
        results.append(operations)
    
    return results

# Taking input from the user
t = int(input("Enter the number of test cases: "))
test_cases = []
for _ in range(t):
    n = int(input("Enter the size of the array: "))
    array = list(map(int, input("Enter the elements of the array: ").split()))
    test_cases.append((n, array))

# Get the output results
output = min_operations_to_max(t, test_cases)


print("\nOutput:")
for result in output:
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
