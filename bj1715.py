n = int(input())
a = []
b = 0
for i in range(n):
    a.append(int(input()))

a.sort()

for i in a:
    b = b + i # 0+10 /10+20/30+40