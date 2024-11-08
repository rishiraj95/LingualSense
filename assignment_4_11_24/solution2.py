def min_operations_to_max():
    T = int(input("Enter number of test cases: "))  # Number of test cases

    results = []  # List to store results for each test case

    for _ in range(T):
        N = int(input("\nEnter the size of the array: "))  # Size of the array
        A = list(map(int, input("Enter the elements of the array: ").split()))  # Elements of the array
        
        min_value = min(A)  # Find the smallest value in the array
        max_value = max(A)  # Find the largest value in the array
        
        if min_value == max_value:
            results.append(0)  # If smallest value is already the largest, no operations needed
        else:
            results.append(A.count(min_value))  # Count occurrences of the smallest value
    
    # Print the results for each test case
    print("\nResults:")
    for result in results:
        print(result)

# Run the function
min_operations_to_max()
