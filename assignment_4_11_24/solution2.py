# Function to solve the problem for each test case
def min_to_max_operations(n, A):
    min_value = min(A)
    # Count elements greater than the minimum value
    operations_needed = sum(1 for x in A if x > min_value)
    return operations_needed

# Main function to handle multiple test cases
def main():
    T = int(input("Enter number of test cases: "))
    results = []
    
    for _ in range(T):
        # Read the size of the array
        n = int(input("Enter the size of the array: "))
        # Read the array elements
        A = list(map(int, input(f"Enter {n} space-separated integers for the array elements: ").split()))
        
        # Calculate the minimum operations needed for this test case
        result = min_to_max_operations(n, A)
        results.append(result)
    
    # Print all results, one per line
    print("Results:")
    for res in results:
        print(res)

# Run the main function
if __name__ == "__main__":
    main()
