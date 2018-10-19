n, k = list(map(int, input().split()))
l = list(map(int, input().split()))
l.append(0)
l.append(0)
dp = [0] * (n+5)
dp2 = [0] * (n+5)
dp3=[0]*(n+55)
dp[k-1]=0
dp[k]=l[k]
for i in range(k+1,n):
    dp[i] = l[i] + max(dp[i - 1], dp[i - 2])
dp2[0]=0
dp2[1]=l[1]
for i in range(2, n):
    dp2[i] = l[i] + max(dp2[i - 1], dp2[i - 2])
for i in range(2, n):
    dp3[i] = dp2[i]-l[i]+l[0]
max1=-1000000000
for i in range(k-1, n):
    s=dp[i]
    r=dp3[i]
    if(s+r>max1):
        max1=s+r
print(max1)
