for _ in range(int(input())):
    n = int(input())
    l = [int(y) for y in input().split()]
    count,t=1,0
    ans=0
    for i in range(n-1):
        if l[i]<=l[i+1]:
            count+=1
        else:
            ans+=(count*(count-1))//2

            count=1
    ans+=(count*count-1)//2
    print(ans+n)
