n = int(input())
m = list(map(int,input().split(' ')))

for i in range(1, n):
    m[i] = max(m[i], m[i] + m[i - 1])   #-4,-4+10 ->6/ 3,3+6 -> 9

print(max(m))

