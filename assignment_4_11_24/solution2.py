# Read the size of the array
N = int(input())

# Read the array elements
A = list(map(int, input().split()))

# Find the minimum value in the array
M = min(A)

# Count how many elements are greater than the minimum value
# operations = sum(1 for x in A if x > M)
operations = 0
for i in A:
    if i > M:
        operations += 1

# Output the number of operations needed
print(operations)
