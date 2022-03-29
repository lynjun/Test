n = int(input())
cnt = 0
for i in range(1,n+1):
    if i <100:
        cnt += 1
    elif i == 1000:
        continue
    else:
        num =[]
        for j in str(i):
            num.append(int(j))

        t = num[0] - num[1]
        d = num[1] - num[2]

        if t == d:
            cnt +=1
print(cnt)



