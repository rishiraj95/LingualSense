# Function to process each test case
def can_reduce_to_one_element(N, K, A):
    # Check if there's any element ≤ K
    for a in A:
        if a <= K:
            return "YES"
    return "NO"

# Reading the number of test cases
T = int(input("Enter number of test cases: "))

# Processing each test case individually
for _ in range(T):
    # Reading N and K for the current test case
    N, K = map(int, input("Enter N and K: ").split())
    # Reading the array A for the current test case
    A = list(map(int, input("Enter elements of array A: ").split()))
    
    # Output the result for this test case
    print(can_reduce_to_one_element(N, K, A))
