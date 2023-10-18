# baekjoon 15651
# N과 M (3)

N, M = list(map(int, input().split()))

p = []

def solution(N, M):
    global p
    if M == 0:
        print(' '.join(p))
        return
    
    for i in range(1, N+1, 1):
        p.append(str(i))
        solution(N, M-1)
        p = p[:-1]
        
solution(N, M)
