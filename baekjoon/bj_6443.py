# baekjoon 6443
# 애너그램

from collections import Counter

N = int(input())
words = [ input() for _ in range(N) ]
p = ''

def solution(counter, depth, p):
    if depth == 0:
        if p not in ana: # no duplicate
            ana.add(p)
            return
    
    for i in counter.keys(): 
        if counter[i] > 0:
            counter[i] -= 1
            p += i
            solution(counter, depth-1, p)
            
            counter[i] += 1
            p = p[:-1]
            
for i in words:
    ana = set()
    counter = Counter(i) # alphabet and the number of it
    solution(counter, len(i), p)
    for a in sorted(ana): # order by alphabet
        print(a)
