# baekjoon 9095
# 1, 2, 3 더하기

import collections

T = int(input())
testcase = [ int(input()) for _ in range(T) ]
dp = collections.defaultdict(int)

def solution(t):
    if t <= 2: # 1과 2는 각각 1, 2
        return t
    if t == 3: # 3은 다시 1과 2로 표현 가능(+1)
        return 4
        
    if dp[t]: # 저장한 값이 존재한다면
        return dp[t]
        
    dp[t] = solution(t-1) + solution(t-2) + solution(t-3)
    return dp[t]

for t in testcase:
    print(solution(t))
