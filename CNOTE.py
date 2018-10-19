for _ in range(int(input())):
    x, y, k, n=list(map(int,input().split()))
    p1 = []
    c1 = []
    s=1
    for i in range(n):
        p, c =list(map(int,input().split()))
        p1.append(p)
        c1.append(c)
    for i in range(n):
        p1[i] += y
    for i in range(n):
        if p1[i]>=x and c1[i]<=k:
            s=0
            break

    if s == 0:
        print("LuckyChef")
    else:
        print('UnluckyChef')

