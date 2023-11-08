# baekjoon 2579
# 계단 오르기

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
