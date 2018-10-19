for _ in range(int(input())):
    n=int(input())
    y=0
    l=[int(y) for y in input().split()]

    DP=[1]*len(l)
    i=0
    while(i<n-1):
        #if l[i]*l[i+1]
        if l[i]*l[i+1]<0 :
            DP[i]+=1
            i+=1
        else:
            DP[i]=DP[i+1]+1
            i+=1
    print(DP)
