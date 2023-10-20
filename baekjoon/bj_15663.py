# baekjoon 15663
# N과 M (9)

N, M = list(map(int, input().split()))
nums = list(map(int, input().split()))
nums = sorted(nums) # asc

p = [] 
visited = [False] * len(nums) # check if it is visited index

def solution(M):
    global p
    global visited
    pre = 0 # previously visited number
    
    if M == 0:
        print(' '.join(p))
        return
    
    for i in range(N):
        # not visited index and not duplicate number of previous 
        if visited[i] == False and nums[i] != pre: 
            p.append(str(nums[i]))
            visited[i] = True # visited index
            solution(M-1)
            pre = nums[i] 
            visited[i] = False # not visited       
            p = p[:-1]

solution(M)
