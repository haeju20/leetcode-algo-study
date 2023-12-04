# baekjoon 10819
# 차이를 최대로

N = int(input())
A = list(map(int, input().split()))

p = []
maxVal = int(-1e9)
visited = [False] * N

# calculate the sum
def calculate(p): 
    sum = 0
    for i in range(N-1):
        sum += abs(p[i] - p[i+1])
      
    return sum

def solution(depth):
    global p, maxVal

    if depth == N:
        maxVal = max(maxVal, calculate(p))
        return

    for i in range(N):
        if not visited[i]: # no duplicate
            p.append(A[i])
            visited[i] = True
            solution(depth+1)
            p.pop()
            visited[i] = False

solution(0)
print(maxVal)
