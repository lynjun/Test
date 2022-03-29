n = int(input())
data = list(map(int,input().split()))
data.sort()
a = 0
b = []
for i in data:
    a = a +i
    b.append(a)

print(sum(b))
