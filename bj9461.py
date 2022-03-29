
d = [0]*101
d[1] = 1
d[2] = 1
d[3] = 1

for i in range(0,98):
    d[i+3] = d[i] + d[i+1]
p = int(input())
for j in range(p):
    n = int(input())
    print(d[n])




