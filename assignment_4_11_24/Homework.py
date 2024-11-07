arr = [1, -3, 5, -2, 1, -3, 7]
ans = arr[0]
for i in range(len(arr)):
    sum=0
    for j in range(i,len(arr)):
        sum += arr[j]
        if sum>ans:
            ans=sum
print(ans)