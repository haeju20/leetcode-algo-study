# baekjoon 6603
# 로또

def solution(depth, M):
    global p
    
    if M == 0: # generate all 6 numbers
        print(' '.join(p))
        return
    
    for i in range(depth, k):
        p.append(str(S[i]))
        solution(i+1, M-1) # from next index
        p = p[:-1]
            
while True:
    nums = list(map(int, input().split()))
    
    k = nums[0]
    if k == 0:
        break
        
    S = nums[1:]
    p = []
    solution(0, 6)
    print()
