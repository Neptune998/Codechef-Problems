for _ in range(int(input())):
    n, k = list(map(int, input().split(' ')))
    l = [int(y) for y in input().split(' ')]
    l.sort()
    sum = 0
    for i in range(n - k, n):
        sum += l[i]
    print(sum)
