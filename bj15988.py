t = int(input())
d= [0] * 1000001
d[0] = 1
d[1] = 2
d[2] = 4


for i in range(3,1000001):
    d[i] = (d[i-1] + d[i-2] + d[i-3]) % 1000000009

for i in range(t):
    n = int(input())

    print(d[n-1]%1000000009)
