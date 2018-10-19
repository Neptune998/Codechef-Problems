for _ in range(int(input())):
  n, m, x, y = list(map(int, input().split(' ')))
  n1 = 1
  m1 = 1
  if n == x and m == y:
    print("Chefirnemo")
  elif n+1 == x and m+1 == y:
    print("Chefirnemo")
  elif x != 1 and y != 1:
    n1 = (n-1) % x
    m1 = (m-1) % y
    if n1 == 0 and m1 == 0:
        print("Chefirnemo")
    elif n1 == 1 and m1 == 1:
        print("Chefirnemo")
    else:
        print('Pofik')
  elif x == 1 and y == 1:
    print('Chefirnemo')
  else:
    if x == 1:
        m1 = (m-1) % y
        if (m1 == 0 or m1 == 1) and n > 1:
            print('Chefirnemo')
        else:
            print('Pofix')
    if y == 1:
        n1 = (n-1) % x
        if (n1 == 0 or n1 == 1) and m > 1:
            print('Chefirnemo')
        else:
            print('Pofik')

