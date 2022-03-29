n,k = map(int,input().split())
b= []
c= []
cnt = 0
for i in range(n):
    a = int(input())
    b.append(a)

b.sort(reverse=True)

for i in b:
    if k//i >= 1:
        z = k//i   #4
        k = k % i
        c.append(z)
    if k == 0:
        break

print(sum(c))
