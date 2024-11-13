# Function to calculate minimum operations for each test case
def min_operations_to_make_min_max(N, A):
    # Find the minimum value in the array
    min_value = min(A)
    
    # Count the elements greater than the minimum value
    operations_needed = sum(1 for x in A if x > min_value)
    
    return operations_needed

# Reading number of test cases
T = int(input("Enter number of test cases: "))

# Processing each test case
results = []
for _ in range(T):
    # Read the size of the array
    N = int(input("Enter size of array: "))
    # Read the array elements
    A = list(map(int, input("Enter array elements: ").split()))
    
    # Get the result for the current test case
    results.append(min_operations_to_make_min_max(N, A))

# Output all results for each test case
print("\n".join(map(str, results)))