for _ in range(int(input())):
    n = int(input())
    l = [int(y) for y in input().split()]
    S=sum(l)
    le=len(l)
    mn=min(l)
    print(S-le*mn)