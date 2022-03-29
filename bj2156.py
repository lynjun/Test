import sys
input = sys.stdin.readline

data = []

n = int(input())
for _ in range(n):
    data.append(int(input()))

d = [0] * n

if n == 1:
    print(data[0])
elif n == 2:
    print(data[0]+data[1])

else:
    d[0] = data[0]
    d[1] = data[0] +data[1]


    for i in range(2,n):
        d[i] = max(data[i]+d[i-2],data[i]+data[i-1]+d[i-3],d[i-1])

    print(d[n-1])

