import sys
for _ in range(int(input())):
    a1=list(input())
    a2=list(input())
    count=0
    DP1=[0]*len(a1)
    DP2=[0]*len(a1)
    n=len(a1)
    for i in range(n):
        if a1[i] == "#" and a2[i] == "#":
            print("No")
            count=1
            break
    if count!=1:
        if a1[0]=="#":
            DP1[0]=sys.maxsize
        if a2[0]=="#":
            DP2[0]=sys.maxsize
        for i in range(1,n):
            if a1[i]!="#":
                DP1[i]=min(DP1[i-1],DP2[i-1]+1)
            else:
                DP1[i]=sys.maxsize
            if a2[i]!="#":
                DP2[i]=min(DP2[i-1],DP1[i-1]+1)
            else:
                DP2[i]=sys.maxsize
        print("Yes")
        re=min(DP1[-1],DP2[-1])
        print(re)



