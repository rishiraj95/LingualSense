def can_reduce_array(A, K):
    A.sort()
    if len(A) > 1 and A[0] + A[1] > K:
        return "NO"
    return "YES"

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(can_reduce_array(A, K))