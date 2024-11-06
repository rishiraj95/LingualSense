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
    print(result)
