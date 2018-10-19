for _ in range(int(input())):
    n = int(input())
    cnt = 0
    l = [int(y) for y in input().split(' ')]

    ls = list(set(l))
    f={}
    for i in range(len(ls)) :
       f[ls[i]] = 0

    for i in range(len(l)):
        f[l[i]] += 1
    for i in range(len(ls)):
        ls[i] *= 2
    for i in range(len(l)):
        if l[i]+l[i+1] in ls:
            cnt+=1

