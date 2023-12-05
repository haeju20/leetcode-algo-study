# baekjoon 1987
# 알파벳

# 시간 초과
R, C = map(int, input().split())
board = [ list(input()) for _ in range(R) ]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

char = set() # less time complexity than list
maxVal = 0

def solution(x, y, cnt):
    global maxVal, char
    
    maxVal = max(maxVal, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in char:
            char.add(board[nx][ny])
            solution(nx, ny, cnt+1)
            char.remove(board[nx][ny]) # remove the visited alphabet -> previous step (bfs)
            
char.add(board[0][0])        
solution(0, 0, 1)

print(maxVal)

# 아래는 틀린 풀이

# maxVal = []
# char = []
# cnt = 0

# def solution(x, y):
#     global maxVal, char, cnt
    
#     if x < 0 or y < 0 or x >= R or y >= C: 
#         return
    
#     if board[x][y] in char:
#         maxVal.append(cnt)
#         return
        
#     char.append(board[x][y])
#     cnt += 1
        
#     solution(x, y+1)
#     solution(x, y-1)
#     solution(x+1, y)
#     solution(x-1, y)

# solution(0, 0)
