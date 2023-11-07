# baekjoon 1932
# 정수 삼각형



# 틀린 코드
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
