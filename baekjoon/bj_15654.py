# baekjoon 15654
# N과 M (5)

N, M = list(map(int, input().split()))
nums = list(map(int, input().split()))
nums = sorted(nums) # asc
p = []

def solution(M):
    global p
    
    if M == 0:
        print(' '.join(p))
        return
    
    for i in range(N):
        if str(nums[i]) not in p: # no duplicate
            p.append(str(nums[i]))
            solution(M-1)
            p = p[:-1]

solution(M)
