# baekjoon 15683
# 감시

import collections
import sys
import copy

N, M = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N) ]
cctv = []
for i in range(N):
    for j in range(M):
        if 0 < info[i][j] < 6:
            # location and type of cctv
            cctv.append([i, j, info[i][j]]) 
            
# up, right, down, left
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cctv_dir = [
    [[0], [1], [2], [3]], # 1 one direction
    [[0, 2], [1, 3]], # 2 verticle or horizontal
    [[0, 1], [1, 2], [2, 3], [0, 3]], # 3 perpendicular
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]], # 4 three directions
    [[0, 1, 2, 3]]] # 5 four directions

min_spot = int(1e9)  

def observation(n, m, d, temp): 
    for i in d: 
        nx, my = n, m 
        while True:
            nx += dx[i]
            my += dy[i]
            
            # if the index is out of range or the location is wall 
            if nx < 0 or nx >= N or my < 0 or my >= M or temp[nx][my] == 6: 
                break
                
            # if the location is already visited 
            if temp[nx][my] == 7:
                continue
        
            temp[nx][my] = 7 # visited
    
def dfs(info, depth): # use depth to count cctv
    global min_spot
    # count all of the cctvs
    if depth == len(cctv):
        # then find min value of blind spot
        min_spot = min(min_spot, find_spot(info))
        return

    n, m, cctv_type = cctv[depth] 
    
    # all the possible directions of the cctv_type
    for d in cctv_dir[cctv_type-1]:
        # initialize the temp to look other directions
        temp = copy.deepcopy(info)
        observation(n, m, d, temp)
        dfs(temp, depth + 1)
        
def find_spot(info): # count 0, blind spot
    count = 0
    for i in range(N):
        for j in range(M):
            if info[i][j] == 0: 
                count += 1
    return count

dfs(info, 0)
print(min_spot)
