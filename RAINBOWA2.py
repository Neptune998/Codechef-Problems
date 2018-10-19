for _ in range(int(input())):
    n=int(input())
    l=[int(y) for y in input().split(' ')]

    l2=[]
    for i in range(n):
        l2.append(l[i])
    md=n//2
    l3=l[0:md]
    l4=l[md+1:n]
    s=0
    for i in range(1,7):
        if i not in l3:
            s=1
        if i not in l4:
            s=1
    t=0
    if 7 not in l2:
        t=1
    u=0
    for i in range(md-2):
        if l3[i]>l3[i+1]:
            u=1
    for i in range(md-2):
        if l4[i]<l4[i+1]:
            u=1
    v=0
    for i in range(md):
        if l2[i]!=l2[n-i-1]:
            v=1
    w=0
    if l2[md]<7:
        w=1
    if s==0 and t==0 and u==0 and v==0 and w==0:
        print("yes")
    else:
        print("no")
