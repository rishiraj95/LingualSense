"""
    problem statement:
    Determine the minimum number of operations required to make the minimum value in the array the maximum value.

    N (int): The size of the array.
    arr (list): The array of integers.

    Returns:
    int: The minimum number of operations required.
"""
def min_to_max(N, arr):

    # Find the minimum value in the array 
    min_value = min(arr)

    # Count how many elements in the array are greater than the minimum value
    count_greater = sum(1 for x in arr if x > min_value)

    # Return the count of elements greater than the minimum value
    return count_greater

# Main loop to handle multiple test cases
t = int(input("Enter number of test cases: "))  # Read number of test cases
for case_number in range(1, t + 1):
    # Get N (size of the array) and discard any other input on the same line if provided
    input_line = input(f"Enter size of array for test case {case_number}: ").split()
    N = int(input_line[0])

    # Get the array elements for the current test case
    arr = list(map(int, input(f"Enter array elements for test case {case_number}: ").split()))

    # Call the min_to_max function to get the result (number of operations)
    result = min_to_max(N, arr)

    # Print the result 
    print(f"Test case {case_number}: The minimum number of operations required is {result}.")
