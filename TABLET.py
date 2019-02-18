for _ in range(int(input())):
    n,b=list(map(int,input().split()))
    ans=[]
    for i in range(n):
       w,h,p=list(map(int,input().split()))
       if p<=b:
          ans.append(w*h)
    if len(ans)==0:
        print("no tablet")
    else:
        print(max(ans))