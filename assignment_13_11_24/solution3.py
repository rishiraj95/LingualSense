test_cases = int(input())
outcome = []
for _ in range(test_cases):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    if N == 1:
        outcome.append("YES")
    else:
        arr.sort()
        if arr[-1] + arr[-2] <= K:
            outcome.append("YES")
        else:
            outcome.append("NO")
print("\n".join(outcome))