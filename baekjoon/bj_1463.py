# baekjoon 1463
# 1로 만들기

import collections

X = int(input())
dp = collections.defaultdict(int)

for num in range(2, X+1): # dp[1] = 0
    dp[num] = dp[num-1] + 1 # 3. 1을 뺀다
    if num % 3 == 0: # 1. 3으로 나눈다
        dp[num] = min(dp[num], dp[num//3]+1) # '3. 1을 뺀다'와 비교
        
    if num % 2 == 0: # 2. 2로 나눈다
        dp[num] = min(dp[num], dp[num//2]+1) # '3. 1을 뺀다'와 비교
        
print(dp[X])
