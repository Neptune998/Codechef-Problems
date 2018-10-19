for _ in range(int(input())):
    e, c = list(map(int, input().split(' ')))
    l = [int(y) for y in input().split(' ')]
    sm = sum(l)
    if sm <= c:
        print("Yes")
    else:
        print("No")
