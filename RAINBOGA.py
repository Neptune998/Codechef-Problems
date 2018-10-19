t=int(input())
for o in range(t):
    n = int(input())
    l = [int(y) for y in input().split(' ')]
    l3=[]
    for i in range(n):
        l3.append(l[i])
    md = len(l) // 2
    l1 = l[0:md]
    l2 = l[md + 1:len(l)]
    f=0
    if min(l3)<7:
        f=1
    m=0
    if n<7:

        m=1
    g=1
    if n%2!=0:
      g=0
    s=0
    if 7 not in l3:
        s=1
    v=0
    for w in range (1,md):
        if l1[w-1]>l1[w]:
            v=1

    t=0
    for d in range(1,7):
        if d not in l1:
            t=1
        if d not in l2:
            t=1
    u=0
    for e in range(0,n):
        if 7 not in l3:
            u=1

    if u==0 and m==0 and f==0 and v==0 and t==0 and s==0 and g==0:
        print("yes")
    else:
        print("no")
