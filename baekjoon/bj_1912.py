# baekjoon 1912
# 연속합

import collections

n = int(input())
p = list(map(int, input().split()))

maxVal = p[0]

for i in range(1, n): # 1, ..., n-1
    p[i] = max(p[i-1]+p[i], p[i]) # find max between sum of the numbers before and current number only
    maxVal = max(maxVal, p[i])
    
print(maxVal)

# 틀린 코드
# n = int(input())
# p = list(map(int, input().split()))

# dp = collections.defaultdict(int)
# maxVal, dp[0] = p[0], p[0]

# for i in range(1, n):
#     dp[i] = max(dp[i-1]+p[i], p[i-1]+p[i])
#     maxVal = max(maxVal, dp[i])
