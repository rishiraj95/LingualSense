def solve():
    n, k = map(int, input("Enter N and K (space-separated): ").split())
    a = list(map(int, input("Enter array A with N space-separated integers: ").split()))

    if n == 1:
        print("YES")
        return

    min_val = min(a)
    possible = True

    for x in a:
        if x + min_val > k:
            possible = False
            break

    if possible:
        print("YES")
    else:
        print("NO")


t = int(input("Enter the number of test cases: "))
for _ in range(t):
    solve()
