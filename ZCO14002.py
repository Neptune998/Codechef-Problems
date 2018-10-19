#an is included
n=int(input())
l=list(map(int,input().split()))
DP=[0]*n
for i in range(n):
   if n==1:
      DP[i]=l[0]
   if n==2:
      DP[i]=l[2]
   if n==3:
       DP[i]= l[3]
   if n==4:
       DP[i]=l[4]+min(l[1],l[2],l[3])
   else:
       #for i in range(len(len(l))):
       DP[i]=(l[i]+min(DP[i-3],DP[i-2],DP[i-1]))
ans=min(DP[n-3],DP[n-2],DP[n-1])
       #print(ans)
print(ans)
