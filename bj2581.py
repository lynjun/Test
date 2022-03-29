m = int(input())
n = int(input())
b = []
for i in range(m,n+1):
    cnt = 0
    for j in range(1,i+1):
        if i % j == 0:
            cnt += 1
            if cnt > 2:
                break
    if cnt == 2:
        b.append(i)
if len(b) !=0:
    print(sum(b))
    print(min(b))
else:
    print('-1')







