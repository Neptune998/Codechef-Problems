for _ in range(int(input())):
    n = int(input())
    x = [1 for i in range(0, n)]
    l = [int(y) for y in input().split()]
    i = n - 2
    if n==1:
        print(1)
        break
    else:
        while i >= 0:
            if l[i]<=l[i + 1]:
                x[i] = x[i + 1] + 1
            i -= 1
        s = sum(x)
        print(s)


