for _ in range(int(input())):
   n, k = list(map(int, input().strip().split(' ')))
   l = [int(y) for y in input().strip().split(' ')]
   re=[]
   for i in range(n):
       if l[i]<=k:
           k-=l[i]
           re.append("1")
       else:
           re.append("0")
   print(''.join(re))