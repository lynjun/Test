n = int(input())
p = []

for i in range(n):
    a = int(input())
    if a == 0:
        p.pop()
    else:
        p.append(a)
print(sum(p))