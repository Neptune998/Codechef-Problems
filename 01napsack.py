n=int(input())
l=[int(y) for y in input().split(' ')]
l1=[]

for i in range(n-1):
   if l[i]==l[i+1]-1:
