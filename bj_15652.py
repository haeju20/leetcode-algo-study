# baekjoon 15652
# N과 M (4)

N, M = list(map(int, input().split()))

p = []

def solution(N, M):
    global p
    if M == 0:
        print(' '.join(p))
        return
    
    for i in range(1, N+1, 1):
        if len(p) > 0 and i < int(p[-1]): # desc
            continue
        p.append(str(i)) # not desc
        solution(N, M-1)
        p = p[:-1]
        
solution(N, M)
