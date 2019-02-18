for _ in range(int(input())):
    n=int(input())
    a=[int(y) for y in input().split()]
    a.sort()
    cnt=0
    for i in range(n):
        if a[i]<=cnt:
            cnt+=1
    print(cnt)