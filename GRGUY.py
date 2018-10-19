for _ in range(int(input())):
    l1=input()
    l2=input()
    a1=list(l1)
    a2=list(l2)
    if a1[0]=="#" and a2[0]=="#":
            print("No")
            break
    i=1
    count=0
    n=len(a1)
    while i<n:
        if a1[i] == "#" and a2[i] == "#":
            print("No")
            break
            i+=1
        if a1[i]=="#" and a2[i]!="#" or a2[i]=="#" and a1[i]!="#" :
            if a1[i+1]!="." or a2[i+1]!=".":
            count+=1
        i+=1
    print("Yes")
    print(count)



