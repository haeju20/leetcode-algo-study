# baekjoon 15657
# N과 M (8)

N, M = list(map(int, input().split()))
nums = list(map(int, input().split()))
nums = sorted(nums) # asc
p = []

def solution(depth, M):
    global p
    
    if M == 0:
        print(' '.join(p))
        return
    
    for i in range(depth, N):
        p.append(str(nums[i]))
        solution(i, M-1) # greater than or equal
        p = p[:-1]

solution(0, M)
