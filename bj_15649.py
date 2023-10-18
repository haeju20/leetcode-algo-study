# backjoon 15649
# N과 M (1)

N, M = list(map(int, input().split()))

p = []

def solution(N, M):
    global p 
    if M == 0:
        print(' '.join(p))
        return
    
    for i in range(1, N+1, 1):
        if str(i) not in p: # no duplicate value (1 1 or 2 2 ...)
            p.append(str(i))
            solution(N, M-1) # M-1 numbers 
            p = p[:-1]
        
solution(N, M)
