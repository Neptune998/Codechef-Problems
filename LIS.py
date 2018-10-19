for _ in range(int(input())):
    n = int(input())
    DP = [1 for i in range(0, n)]
    l = [int(y) for y in input().split()]
    for i in range(len(l)):
        j=0
        while j<i:
                if l[j]<l[i]:
                   DP[i]=max(DP[i],DP[j]+1)
                   j+=1
                else:
                    j+=1

    print(max(DP))
