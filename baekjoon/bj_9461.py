# baekjoon 9461
# 파도반 수열

import collections

T = int(input())
N = [ int(input()) for _ in range(T)]

dp = collections.defaultdict(int)
dp[1], dp[2], dp[3] = 1, 1, 1 # n is length of the side -> start from 1

def solution(n):
    if dp[n]:
        return dp[n]
    
    dp[n] = solution(n-2) + solution(n-3)
    return dp[n]

for n in N:
    print(solution(n))
