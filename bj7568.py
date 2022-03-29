n = int(input())

p = []
r = []
for _ in range(n):
    w,h = map(int,input().split())
    p.append((w,h))

for i in range(n):
    cnt = 0

    for j in range(n):
        if p[i][0] < p[j][0] and p[i][1] <p[j][1]:
            cnt +=1
        r.append(cnt+1)

for i in r:
    print(r,end='')



