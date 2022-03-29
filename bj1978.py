n= int(input())
a = list(map(int,input().split()))   # 3 7 5 9 13
count = 0
for i in a: # 3 7 5 9 13
    cnt = 0
    for j in range(1,i+1):    # 1 3 5 7
        if i % j == 0:
            cnt += 1
            if cnt > 2:
                break
    if cnt == 2:
        count += 1
print(count)
