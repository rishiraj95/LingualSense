def can_reduce_to_one_element(T, test_cases):
    results = []
    for _ in range(T):
        N, K = test_cases[_][0]
        A = test_cases[_][1]
        if N == 1:
            results.append("YES")
            continue
        A.sort()
        if A[0] + A[1] <= K:
            results.append("YES")
        else:
            results.append("NO")
    return results

T = int(input())
test_cases = []
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    test_cases.append(((N, K), A))

results = can_reduce_to_one_element(T, test_cases)
print("\n".join(results))
