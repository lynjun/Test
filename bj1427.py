n = int(input())

a = []

for i in range(n):
    b,c = map(int,input().split())
    a.append((b,c))

a.sort()

for i in range(n):
    print(a[i][0],a[i][0])