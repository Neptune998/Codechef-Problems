for i in range(int(input())):
    n, m = list(map(int, input().split()))
    l = [int(y) for y in input().split(' ')]
    chef = 0
    ass = 0
    cntc = []
    cntass = []
    for i in range(1, n+1):
        if i not in l and chef == 0:
            chef = 1
            ass = 0
            cntc.append(i)
        elif i not in l and ass == 0:
            chef = 0
            ass = 1
            cntass.append(i)
    print(" ".join(map(str, cntc)))
    print(" ".join(map(str, cntass)))