# To reduce element, either YES or NO

# This function is to analyse element reduction
def reduce_element(N, K, A):

    #if N is already 1 then print yes
    if N == 1:
        return "YES"
    
    #first we sort the array
    A.sort()
    
    #if the sum is ledd than given value K, it can be reduced so print YES or else NO
    if A[0] + A[1] > K:
        return "NO"
    else:
        return "YES"

#take input
T = int(input())
res = []
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    res.append(reduce_element(N, K, A))

#print the result
print("\n".join(res))
