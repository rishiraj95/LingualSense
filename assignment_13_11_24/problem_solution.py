def can_reduce_to_one_element(test_cases):
    results = []
    for case in test_cases:
        N, K = case[0]
        A = case[1]
        
        if N == 1:
            results.append("YES")
            continue
        
        max_A = max(A)
        min_A = min(A)
        
        if max_A > K:
            results.append("NO")
        elif 2 * min_A <= K:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Input reading
T = int(input())
test_cases = []
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    test_cases.append(((N, K), A))

# Process and output results
results = can_reduce_to_one_element(test_cases)
for result in results:
    print(result)
