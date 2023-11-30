# baekjoon 2839
# 설탕 배달

import collections

N = int(input())

dp = collections.defaultdict(int) 

# initialize the values before 6
dp[3], dp[5] = 1, 1
dp[1], dp[2], dp[4] = -1, -1, -1

if N <= 5: 
    print(dp[N])
    exit()

for n in range(6, N+1): # if N is bigger than 5
    if dp[n-5] != -1 and dp[n-3] != -1:
        dp[n] = min(dp[n-5] + 1, dp[n-3] + 1)
        
    elif dp[n-5] != -1:
        dp[n] = dp[n-5] + 1
        
    elif dp[n-3] != -1:
        dp[n] = dp[n-3] + 1
        
    else:
        dp[n] = -1
   
print(dp[N])
