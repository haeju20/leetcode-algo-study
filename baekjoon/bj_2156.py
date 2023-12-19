# baekjoon 2156
# 포도주 시식

import collections

n = int(input())
wine = [ int(input()) for _ in range(n) ]

dp = collections.defaultdict(int)

if n < 3:
    print(sum(wine))
    exit()

# initialize the value
dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
dp[2] = max(dp[1], wine[0] + wine[2], wine[1] + wine[2])

for i in range(3, n):
    dp[i] = max(dp[i-2]+wine[i], dp[i-3]+wine[i-1]+wine[i], dp[i-1])

print(dp[n-1])
