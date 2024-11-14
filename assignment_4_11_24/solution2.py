t = int(input())
answers = []

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    min_val =min(arr)
    max_val =max(arr)
    ops =0
    
    if min_val != max_val:
        for num in arr:
            if num > min_val:
                ops += 1
    
    answers.append(str(ops))

print("\n".join(answers))
