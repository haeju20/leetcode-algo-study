# baekjoon 11052
# 카드 구매하기

import collections

N = int(input())
p = list(map(int, input().split()))
dp = collections.defaultdict(int)

for i in range(1, N+1): # 1, 2, ... N
    dp[i] = p[i-1] # P as initial value
    for j in range(1, i+1): # 1, 2, ..., i
        dp[i] = max(dp[i], dp[i-j] + p[j-1]) 

print(dp[N])
