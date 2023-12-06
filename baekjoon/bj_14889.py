# baekjoon 14889
# 스타트와 링크

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

minVal = int(1e9)
s_visited = [False] * N # start team member
l_visited = [True] * N # link team member

# calculate the sum of S of the team
def calculate(visited):
    sum = 0

    for i in range(N - 1):
        for j in range(i + 1, N):
            if visited[i] and visited[j]:
                # add two values along the diagonal
                sum += S[i][j] + S[j][i]
    return sum


def solution(depth, idx):
    global minVal

    if depth == N // 2:
        start = calculate(s_visited)
        link = calculate(l_visited)
        minVal = min(minVal, abs(start - link))
        return

    for i in range(idx, N):
        s_visited[i] = True
        l_visited[i] = False
        solution(depth+1, i+1)
        s_visited[i] = False
        l_visited[i] = True


solution(0, 0)
print(minVal)
