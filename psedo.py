for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    l=[0]*n
    cnt=0
    for i in range(n):
        l[i]=list(input())
    for i in range(n-1):
      for j in range(m-1):
        '''if l[i][j]=='R'and l[i][j+1]=='R' and l[i][j+2]=='R':
            l[i][j+1]='G'
            cnt+=3
        if l[i][j] == 'R' and l[i][j + 1] == 'R' and l[i][j + 2] == 'G':
            l[i][j] = 'G'
            cnt+=3
        if l[i][j] == 'G' and l[i][j + 1] == 'G' and l[i][j + 2] == 'G':
            l[i][j + 1] = 'R'
            cnt+=5
        if l[i][j] == 'G' and l[i][j + 1] == 'G' and l[i][j + 2] == 'R':
            l[i][j] = 'R'
            cnt+=5'''
        if l[i][j]=='R':
            if l[i][j+1]!='G':
                l[i][j+1]="G"
                cnt+=3
            if l[i+1][j]!="G":
                l[i+1][j]='G'
                cnt+=3
        if l[i][j] == 'G':
            if l[i][j + 1] != 'R':
                l[i][j + 1] = "R"
                cnt += 3
            if l[i + 1][j] != "R":
                l[i + 1][j] = 'R'
                cnt += 3

print(l)
print(cnt)
