# baekjoon 12101
# 1, 2, 3 더하기 2

n, k = map(int, input().split())
p = []
num = []

def solution(depth): # depth is the number of 1, 2, 3
    global p, num

    if depth == 0: 
        if sum(num) == n:
            p.append(num)
        return

    for i in range(1, 4): # using 1, 2, 3 
        if sum(num) <= n:
            num.append(i)
            solution(depth-1)
            num = num[:-1]
        
for i in range(n): 
    solution(i+1)
    
p = sorted(p)

if len(p) >= k-1:
    result = list(map(str, p[k-1]))
    print('+'.join(result))
else:    
    print(-1)
