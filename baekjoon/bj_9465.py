# baekjoon 9465
# 스티커

T = int(input())

for _ in range(T):
    n = int(input())
    score = [ list(map(int, input().split())) for _ in range(2) ] 

    for i in range(1, n):
        for j in range(2): # 0th row and 1st row
            # initialize the value if 1st col
            if i == 1:
                score[j][i] += score[1-j][i-1] 
                continue
                
            # max value so far including current value 
            score[j][i] += max(score[1-j][i-1], score[1-j][i-2])
    
    print(max(score[0][n-1], score[1][n-1]))
