n,m = map(int,input().split())
a = list(map(int,input().split()))
b = []
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if a[i] + a[j] +a[k] <= m:
                c = a[i] + a[j] + a[k]
                b.append(c)
print(max(b))

