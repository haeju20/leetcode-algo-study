# baekjoon 2239
# 스도쿠

# Python 3 에서 시간 초과
# PyPy3 에서 성공

board = [ list(map(int, input())) for _ in range(9)]
empty = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0] 

def check(n, m, num):
    # row check
    for i in range(9):
        if board[i][m] == num:
            return False
    
    # col check
    for i in range(9):
        if board[n][i] == num:
            return False
    
    # 3x3 check
    for i in range((n//3)*3, (n//3)*3+3):
        for j in range((m//3)*3, (m//3)*3+3):
            if board[i][j] == num:
                return False
    
    return True

def solution(depth):
    if depth == len(empty):
        for i in board:
            print(''.join(map(str, i)))
        exit()  
        
    n, m = empty[depth] # (row, col) where the value is 0
    for num in range(1, 10):
        if check(n, m, num): 
            board[n][m] = num
            solution(depth+1)
            board[n][m] = 0

solution(0)
