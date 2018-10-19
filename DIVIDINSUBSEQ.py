n=int(input())

l=[]
for _ in range(n):
    l.append(int(input()))

dp=[1]*n
for i in range(1,n):
    for j in range(0,i):
        if l[i]%l[j]==0 dp[i]<dp[i]+1:
            dp[i]=dp[j]+1
print(max(dp))
