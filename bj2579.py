import sys
input = sys.stdin.readline

arr = []  # 점수

n = int(input())
for _ in range(n):
        arr.append(int(input())) # 10 20 15 25 10 20

dp = [0] * n

if n == 1:
        print(arr[0])
elif n == 2:
        print(arr[0]+arr[1])
else:
        dp[0] = arr[0]
        dp[1] = max(arr[0]+arr[1],arr[1])
        dp[2] = max(arr[0]+arr[2],arr[1]+arr[2])  #25,35

        for i in range(3,n):
                dp[i] = max(arr[i]+dp[i-2],arr[i]+arr[i-1]+dp[i-3])

        print(dp[n-1])

