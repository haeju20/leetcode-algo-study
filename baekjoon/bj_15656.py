# baekjoon 15656
# N과 M (7)

N, M = list(map(int, input().split()))
nums = list(map(int, input().split()))
nums = sorted(nums)
p = []

def solution(M):
    global p
    
    if M == 0:
        print(' '.join(p))
        return
    
    for i in range(N):
        p.append(str(nums[i]))
        solution(M-1)
        p = p[:-1]

solution(M)
