for _ in range(int(input())):
    n=int(input())
    b=[]
    cnt=0
    for i in range(n):
        b.append(bin(i))
    for i in range(n):
        if b[i].count("1")==1:

            cnt+=1
    print(cnt)
    cnt2=0
    while(n!=1):
        n=n//2
        cnt2+=1
    print(cnt2+1)