for _ in range(int(input())):
   n,m=list(map(int,input().split()))
   s1,t1=[],[]
   for i in range(n):
       s,l=list(map(int,input().split()))
       for i in range(s,l):
          s1.append(i)

   for i in range(m):
       t = int(input())
       t1.append(t)
   for i in range(m):
       if t1[i] in s1:
               print(0)
       elif t1[i] not in s1:
           for j in range(0,len(s1)):
               if s1[j]<t1[i]<s1[j]:
                   print(0)
                   break
   for i in range(m):
       if t1[i]<(min(s1)):
           print(min(s1)-t1[i])
   print(t1)