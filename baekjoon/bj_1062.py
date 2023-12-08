# baekjoon 1062
# 가르침

# 시간 초과
N, K = map(int, input().split())
word = []

visited = [False] * 26  # alphabet that student learned
anta = ['a', 'n', 't', 'i', 'c']
cnt_ini = 0  # the number of words that student can read
maxVal = 0

for _ in range(N):
    w = input()
    if w[4:-4] == "":  # antatica
        cnt_ini += 1
        continue
    word.append(w[4:-4])

if K < 5:
    print(0)
    exit()
else:  # K >= 5
    for i in anta:
        visited[ord(i) - 97] = True
        K -= 1

teach = set()
for i in range(N):
    for j in word[i]:
        if not visited[ord(j) - 97]:
            teach.add(j)


def calculate():
    cnt = 0

    for i in word:
        flag = True
        for j in i:
            if not visited[ord(j) - 97]:
                flag = False
        if flag:
            cnt += 1

    return cnt


def solution(depth):
    global maxVal, cnt_ini

    if depth == 0:
        maxVal = max(maxVal, calculate() + cnt_ini)
        return

    for i in teach:
        idx = ord(i) - 97
        if not visited[idx]:
            visited[idx] = True
            solution(depth - 1)
            visited[idx] = False

solution(K)
print(maxVal)
