# baekjoon 1149
# RGB거리

import collections

N = int(input())
dp = collections.defaultdict(int)
cost = []

for _ in range(N):
    p = list(map(int, input().split()))
    cost.append(p)

for i in range(1, N): # value of (i)th row <- the minimum possible value of (i-1)th row + (i)th row
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0]
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + cost[i][1]
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + cost[i][2]

# minimum value of end of the row(sum)
print(min(cost[N-1][0], cost[N-1][1], cost[N-1][2]))
