# baekjoon 20413
# MVP 다이아몬드 (Easy)

def solution(N, mvp, history):
    result = []
    max_money = {} # dictionary
    grade = ['B', 'S', 'G', 'P', 'D']
    for i in range(len(grade) - 1):
        max_money[grade[i]] = mvp[i] - 1
    
    for i in range(N):
        if history[i] == 'D':
            result.append(mvp[3])
            continue            
        if i > 0:
            result.append(max_money[history[i]] - result[i-1])
        else: # i == 0
            result.append(max_money[history[i]])    
    return sum(result)
    
N = int(input())
mvp = list(map(int, input().split()))
history = input()
print(solution(N, mvp, history))
