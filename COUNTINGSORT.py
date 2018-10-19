A,n,k=[1,0,3,4,5,2,2,3,4],9,6
c = [0]*k
b = [0]*(n+1)
for i in range(n):
    c[A[i]] = c[A[i]]+1

for i in range(1, k):
    c[i] = c[i]+c[i-1]

for i in range(n-1, -1, -1):
    b[c[A[i]]] = A[i]
    c[A[i]] -= 1
print(b[1:n+1])
