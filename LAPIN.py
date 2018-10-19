for _ in range(int(input())):
  l=list(input())
  if len(l)%2==0:
     l1=l[0:len(l)//2]
     l2=l[len(l)//2:len(l)]
     l1.sort()
     l2.sort()
     if l1==l2:
        print("YES")
     else:
        print("NO")
  else:
    l1 = l[0:len(l)//2]
    l2 = l[len(l)//2+1:len(l)]
    l1.sort()
    l2.sort()
    if l1 == l2:
        print("YES")
    else:
        print("NO")