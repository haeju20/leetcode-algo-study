# baekjoon 13023
# ABCDE

N, M = map(int, input().split())
f = [[] for _ in range(N)]

for _ in range(M): # create graph 
    a, b = map(int, input().split())
    f[a].append(b)
    f[b].append(a)

visited = [False] * N

def solution(j, cnt):
    if cnt >= 4: 
        print(1)
        exit()
    
    for k in j:
        if visited[k] == False:
            visited[k] = True
            solution(f[k], cnt+1) # f[k] is a set of edges connected to k
            visited[k] = False
          
cnt = 0 # the number of edges(link)
for i in range(N):
    visited[i] = True
    solution(f[i], cnt) # f[i] is a set of edges connected to i
    visited[i] = False
    
print(0)
