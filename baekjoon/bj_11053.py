# baekjoon 11053
# 가장 긴 증가하는 부분 수열

import collections

n = int(input())
A = list(map(int, input().split()))
dp = collections.defaultdict(int) 

for i in range(n):
    for j in range(i):
        # to find max length of subsequence that can be made with current value, A[i] as the last value
        if A[i] > A[j] and dp[j] > dp[i]:
            dp[i] = dp[j] 
    dp[i] += 1 # with current value, A[i]
   
print(max(dp.values()))
