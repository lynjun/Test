n = int(input())

a = [0] * 1001

a[1] = 1
a[2] = 3
a[3] = 5
a[4] = 11

for i in range(5,n+1):
    for j in i:
        a[i] = 5

print(a[n] % 10007)