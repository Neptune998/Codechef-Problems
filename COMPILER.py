for _ in range(int(input())):
    l =list(input())
    open,pair,s=0,0,0
    for i in range(len(l)):
        if l[i]=="<":
            open+=1
        elif l[i]==">" and open<1:
            break
        elif l[i]==">" and open>0:
            open-=1
            if open==0:
                pair=s+1
        else:
            break
        s+=1
    print(pair)