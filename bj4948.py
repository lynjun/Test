
n = int(input())
result = 0
for i in range(n+1,2*n):
    cnt = 0

    for j in range(1,i+1):
        if i % j == 0:
            cnt += 1
            if cnt > 3:
                break
    if cnt == 2:
        result += 1
print(result)