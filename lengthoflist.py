for _ in range(int(input())):
   n,m=list(map(int,input().split()))
   s1,l1,t1,ans=[],[],[],0
   for i in range(n):
       s,l=list(map(int,input().split()))
       s1.append(s)
       l1.append(l)
   for i in range(m) :
       t=int(input())
       t1.append(t)
   for i in range(m):
       ans=0
       if t1[i] in s1:
           print("0")
       elif t1[i] in l1:
           inn=l1.index(t1[i])
           print(s1[inn+1]-l1[inn])
       elif t1[i]>max(l1):
           print("-1")
       elif t1[i]<mi
       else:
           for j in range(n):
               if s1[j]<t1[i]<l1[j]:
                   print("0") 
                   break
