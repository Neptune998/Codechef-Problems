for _ in range(int(input())):
    n = int(input())
    cnt = 0
    l1 = [int(y) for y in input().split(' ')]
    l = []

    for i in range(n):
        if l1[i] not in l:
            l.append(l1[i])
    l.sort()

    for i in range(n-1):
        for j in range(n-1):
            if ((l[i]+l[j])/2) in l and l[i]!=l[j] :

                cnt += 1

    print(cnt-1)