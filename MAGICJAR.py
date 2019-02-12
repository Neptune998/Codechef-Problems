for _ in range(int(input())):
    n=int(input())
    a=[int(y) for y in input().split()]
    sum_a=sum(a)
    ans = (sum_a-n)+1
    print(ans)