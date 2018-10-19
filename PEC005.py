n,k=5,2
l=[5,3,-2,1,1]
dp=[0 for y in range(len(l))]
dp[0]=0
dp[1]=l[k]
print(dp[1])
for i in range(k,n):
    print(i)
    dp[i]=l[i]+max(dp[i-1],dp[i-2])
    print(dp[i])
print(dp)
