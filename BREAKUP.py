n=int(input())
l=list(map(int,input().split()))
DP=[0]*n
DP[0]=1
if l[0]!=l[1]:
        DP[1]=2
else:
        DP[1]=1
for i in range(2,n):
        temp=i
        for j in range(0,i+1):
            S=l[j:i+1]
            a=S[0:len(S)//2]+S[len(S)//2:]
           # print(S)
            S.reverse()
            if S==a:
                temp=min(temp,DP[j-1]+1)
        DP[i]=temp
print(DP[n-1])