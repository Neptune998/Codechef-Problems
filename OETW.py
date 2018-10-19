for _ in range(int(input())):
    n = int(input())
    a, b, l = 0, 0, []
    a = list(map(int, input().split()))
    for i in range(0, n):
        if a[i] == 1:
            a += 1
        else:
            b += 1
        l.append(a[i])
    if a == 0:
        print(b)
    elif b == 0:
        print(a)
    else:
        print(b * 2 + a)

