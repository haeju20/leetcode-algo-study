# baekjoon 11052
# 카드 구매하기

# wrong answer
# import collections

# N = int(input())
# p = list(map(int, input().split()))
# dp = collections.defaultdict(int)

# # initialize
# dp[N], dp[1] = p[N-1], p[0]*N

# for i in range(N-1, 1, -1): 
#     if N % i == 0:
#         dp[i] = (N//i) * p[i-1]
#     elif i > N//2:
#         dp[i] = p[i-1] + p[N-i-1]
#     else:
#         dp[i] = p[i-1] * (N//i) + N%i
      
# print(max(dp.values()))
