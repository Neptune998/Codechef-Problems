for i in range(int(input())):
    n, k = list(map(int,input().strip().split(' ')))
    l = [str(y) for y in input().strip().split(' ')]
    l1=[]
    l2=[]
    for i in range(k):
        l1=[str(y) for y in input().strip().split(' ')]
        temp=l1[1:]
        for i in range(len(temp)):

           l2.append(temp[i])

    cnt=[0]*n

    for i in range(n):
        if l[i] in l2:
            cnt[i]=1

    for i in range(len(cnt)):
        if cnt[i] == 1:
            cnt[i]="YES"
        else:
            cnt[i]="NO"
    print(" ".join(map(str, cnt)))