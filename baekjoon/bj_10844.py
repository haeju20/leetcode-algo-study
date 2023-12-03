# baekjoon 10844
# 쉬운 계단 수

N = int(input())
dp = [ [0 for _ in range(10)] for _ in range(N+1) ] 

for i in range(1, 10): # 1-digit numbers (1~9)
    dp[1][i] = 1
    
for i in range(2, N+1): # from 2-digit numbers
    for j in range(10): # 0, 1, ..., 9
        # the number of i-digit number with j as the last digit number
        # set the recurrence relation
        if j == 0:
            dp[i][j] = dp[i-1][j+1]

        if 1 <= j <= 8:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    
        if j == 9:
            dp[i][j] = dp[i-1][j-1]

print(sum(dp[N]) % 1000000000)    
