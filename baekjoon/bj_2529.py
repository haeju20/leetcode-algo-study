# baekjoon 2529
# 부등호

k = int(input())
A = list(input().split())
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

p = [] # set of values
value = '' # (k+1) digit number
visited = [False] * len(nums) # visit flag of nums list

def calculate(n, m, ineq):   
    if ineq == '<':
        if n > m:
            return False
        else: return True
        
    else: # ineq == '>':
        if n < m:
            return False
        else: return True

def solution(digit):
    global value 
    
    if digit == k+1:
        p.append(value)
        return
    
    for i in range(len(nums)):
        if visited[i]:
            continue
            
        if digit == 0 or calculate(int(value[-1]), nums[i], A[digit-1]):
            value += str(nums[i]) 
            visited[i] = True
          
            solution(digit+1) 
            value = value[:-1] 
            visited[i] = False
    
solution(0)    
    
print(max(p))
print(min(p))
