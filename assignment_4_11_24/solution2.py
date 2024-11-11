def min_operations_to_make_min_max(N, A):
    M = min(A)
    max_value = max(A)
    
    if M == max_value:
        return 0
    else:
        operations = sum(1 for x in A if x > M)
        return operations

N = int(input("Enter the size of the array: "))
A = list(map(int, input("Enter the elements of the array: ").split()))

result = min_operations_to_make_min_max(N, A)
print("Minimum number of operations:", result)
