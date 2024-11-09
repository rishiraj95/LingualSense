def minToMax(N,A):
    n= len(A)
    if n == 1:
        return 0
    minA = min(A)
    maxA = max(A)
    count = 0
    for i in A:
        if minA < i:
            count  += 1
    return count

T = int(input())
result = []
for _ in range(T):
    N =int(input())
    A = list(map(int,input().split()))
    result.append(minToMax(N,A))
print(result)
