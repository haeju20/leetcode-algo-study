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
