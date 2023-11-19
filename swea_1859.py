# 출력 형식 바꾸면 정답
def solution(p):
    maxVal, cnt = p[-1], 0
    for i in range(N-1, -1, -1):
        maxVal = max(maxVal, p[i])
        if maxVal > p[i]:
            cnt += maxVal - p[i]
    print(cnt)

if __name__ == '__main__':
    N = int(input())
    p = list(map(int, input().split()))
    solution(p)

# fail (runtime error)
# N = int(input())
# p = list(map(int, input().split()))
# print(p)
# b = []
# cnt = 0

# for i in range(N-1): 
#     if i == N-2 and p[i] < p[i+1]:
#         b.append(p[i])
#         for j in range(len(b)):
#             cnt += p[i+1] - b[j]
#         b = []
#         continue

#     if p[i] > p[i+1]:
#         for j in range(len(b)):
#             cnt += p[i] - b[j]
#         b = []
        
#     if p[i] <= p[i+1]:
#         b.append(p[i])
        
# print(cnt)
