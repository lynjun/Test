m,n = map(int,input().split())

for i in range(m,n+1):
    cnt = 0
    for j in range(1,i+1):
        if i%j == 0:
            cnt += 1
            if cnt > 3 :
                break
    if cnt == 2:
        print(i)