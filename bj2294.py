a,b = map(int,input().split())   # a - 갯수 , b - 가치의 합
d = []
for _ in range(a):
    d.append(int(input()))  #d = [1,5,12]

dp = [0] + [100001 for _ in range(b)]

for i in d:
    for j in range(1,b+1):
        if j-i >= 0:
            dp[j] = min(dp[j-i]+1,dp[j])
if dp[b] != 100001:
    print(dp[b])
else:
    print(-1)