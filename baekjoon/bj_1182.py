# baekjoon 1182
# 부분수열의 합

N, S = map(int, input().split())
nums = list(map(int, input().split()))
p = [] # subsequence
cnt = 0

def solution(depth, i):
    global p
    global cnt
  
    if i == 0: # one subsequence
        if sum(p) == S: # check the sum of p
            cnt += 1
        return 

    for j in range(depth, N):
        p.append(nums[j])
        solution(j+1, i-1) # call recursive func with index+1, length-1
        p = p[:-1]
        
for i in range(1, N+1): # length of p
    solution(0, i) 
print(cnt)
