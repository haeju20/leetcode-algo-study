# baekjoon 2579
# 계단 오르기

import sys
import collections

n = int(input())
score = [ int(input()) for _ in range(n) ]

maxVal = -sys.maxsize
dp = collections.defaultdict(int)
dp[0] = score[0] # initial value

for i in range(1, n):
    if i == 1:
        dp[i] = dp[i-1] + score[i]
        continue
    if i == 2:
        dp[i] = max(dp[i-2]+score[i], score[i-1]+score[i]) 
        continue
 
    # i: 3, ..., n-1      
    # 2칸 올라온 경우와 1칸 올라온(연속 세 계단 불가하므로 dp[-3]과 더함) 경우를 비교
    dp[i] = max(dp[i-2]+score[i], dp[i-3]+score[i-1]+score[i]) 

print(dp[n-1])

# wrong answer
# n = int(input())
# score = [ int(input()) for _ in range(n) ]

# maxVal = -sys.maxsize
# dp = collections.defaultdict(int)
# dp[0] = score[-1] # initial value

# for i in range(1, n):
#     if i == 1:
#         dp[i] = dp[0] + score[-(1+i)]
#         continue
    
#     if i == 2: # no consecutive values 
#         dp[i] = dp[0] + score[-(1+i)]
#         continue
    
#     # i: 3, ..., n-1      
#     dp[i] = max(dp[i-2]+score[-(1+i)], dp[i-3]+score[-i]+score[-(1+i)])

# print(dp[n-1])
