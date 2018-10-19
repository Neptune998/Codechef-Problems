for _ in range(int(input())):
    n = int(input())
    x = [1 for i in range(0, n)]
    i = n - 2

    l = [int(y) for y in input().split()]
    while i >= 0:

        if l[i] < 0:
            if l[i + 1] > 0:
                x[i] = x[i+1]+1
        elif l[i] > 0:
            if l[i + 1] < 0:
                x[i] =x[i+1]+1
        i -= 1

    print(' '.join(str(x) for x in x))


