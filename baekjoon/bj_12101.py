# baekjoon 12101
# 1, 2, 3 더하기 2

import sys
sys.setrecursionlimit(10**7)

n, k = map(int, input().split())
p = []
num = []

def solution(num):
    global p

    if sum(num) == n:
        print(num, sum(num))
        if num not in p:
            p.append(num)
        return
    
    for i in range(1, 4): # 1, 2, 3
        print('in for [', i, ']: ', num)
        if sum(num) < n:
            num.append(i)
            solution(num)
            if len(num) > 2:
                num = num[:-2]
            else: return
        
for i in range(1, 4):
    num.append(i)
    solution(num)
    num = []
    
p = sorted(p)

if len(p) >= k-1:
    print(p[k-1])
else:    
    print(-1)
    
    
    
