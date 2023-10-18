# baekjoon 15650
# N과 M (2)

N, M = list(map(int, input().split()))

p = []

def solution(N, M):
    global p
    if M == 0 and p == sorted(p): # print asc(already sorted) only 
        print(' '.join(p))
        return
    
    for i in range(1, N+1, 1):
        if str(i) not in p:
            p.append(str(i))
            solution(N, M-1)
            p = p[:-1]
        
solution(N, M)

# N, M = list(map(int, input().split()))

# p = []

# def solution(depth, N, M):
#     global p
#     if M == 0:
#         print(' '.join(p))
#         return
    
#     for i in range(depth, N+1, 1):
#         if str(i) not in p:
#             p.append(str(i))
#             solution(i+1, N, M-1) # give depth as i+1, always bigger than the previous number
#             p = p[:-1]
        
# solution(1, N, M)
