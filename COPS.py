for i in range(int(input())):
    m, x, y = list(map(int, input().strip().split(' ')))
    l = [int(y) for y in input().strip().split(' ')]
    h = ["0"] * 100

    r = x * y
    for i in range(len(l)):
        if r + l[i] > 100:
            rr = 99
        else:
            rr = r + l[i]-1
        if l[i] - r < 1:
            ll = 0
        else:
            ll = l[i] - r-1

        for j in range(ll, rr+1):
                h[j] = "1"

    k = h.count('0')
    print(k)
