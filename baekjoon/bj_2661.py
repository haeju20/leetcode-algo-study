# baekjoon 2661
# 좋은수열

N = int(input())

visited = [-1 for _ in range(3)]
minVal = 0
p = ''

def solution(depth, temp):
    if p[:] == temp:
        return
    
    if depth == N:
        minVal = min(minVal, p)
    
    for i in range(1, 4): # 1, 2, 3
        if depth != 0 and i != p[-1]:
            if visited[i] == -1:
                p += str(i)
                visited[i] = depth
            else: # visited number
                temp = p[visited[i]:depth]
                visited[i] = depth
            
        solution(depth+1, idx, temp)
        visited[i] = False

solution(0, '')
print(minVal)
