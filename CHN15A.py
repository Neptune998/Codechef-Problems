for i in range(int(input())):
    s1=list(map(int,input().split()))
    s2=list(map(int,input().split()))
    s3=list(map(int,input().split()))
    s1.sort()
    s2.sort()
    s3.sort()
    if s1==s2 or s1==s3 or s2==s3:
     print("no")
    else:
       print("yes")