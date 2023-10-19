# baekjoon 15655
# N과 M (6)

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
        if str(nums[i]) not in p: # no duplicate
            p.append(str(nums[i]))
            solution(i, M-1) # always bigger than the previous number
            p = p[:-1]

solution(0, M)
