# baekjoon 1932
# 정수 삼각형

import collections

n = int(input())
tri = [ list(map(int, input().split())) for _ in range(n) ]
dp = collections.defaultdict(list)
dp[0].append(tri[0][0]) # initial value

for row in range(1, n): # row: 1, 2, ..., n-1
    
    if row == 1:
        dp[row].append(dp[row-1][0] + tri[row][0])
        dp[row].append(dp[row-1][0] + tri[row][1])
        continue
    
    # row: 2, ..., n-1
    for idx in range(row+1): # index of the row: 0, 1, ..., row
        if idx == 0: # triangle[row-1][0] only 
            dp[row].append(dp[row-1][idx] + tri[row][idx])
        
        elif idx == row: # triangle[row-1][row] only 
            dp[row].append(dp[row-1][idx-1] + tri[row][idx])
            
        else: # except for the values of both ends
            dp[row].append(max(dp[row-1][idx-1] + tri[row][idx], dp[row-1][idx] + tri[row][idx]))
       
print(max(dp[n-1]))

# 틀린 코드 (시간 초과)
# import sys
# n = int(input())
# triangle = [ list(map(int, input().split())) for _ in range(n) ]

# maxVal = -sys.maxsize

# def solution(idx, sum, pre):
#     global maxVal
    
#     if idx == n-1:
#         maxVal = max(maxVal, sum)
#         return
    
#     for i in range(len(triangle[idx])):
#         if abs(pre-i) < 2:          
#             sum += triangle[idx][i]
#             solution(idx+1, sum, i)
#             sum -= triangle[idx][i]  

# solution(0, 0, 0)
