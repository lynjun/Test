n = int(input()) #10

dp = [0]*10000000



for i in range(2,n+1):

    dp[i] = dp[i-1]+1          #dp[0],dp[1] = 0/ dp[2] = 1/dp[3] =1/dp[4]=2/dp[5] =dp[4]+1 =3
    if i % 3 ==0:
        dp[i] = min(dp[i],dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
for i in range(1,11):
    print(dp[i])
