# baekjoon 1713
# 후보 추천하기

import collections

N = int(input())
r = int(input())
recom = list(map(int, input().split()))

cnt = collections.defaultdict(int)
cand = collections.defaultdict(int) # candidate dict

for i in recom:
    # candidate dict is full and current value i is not in candidate dict
    if len(cand) == N and cnt[i] == 0:
        minIdx = [] # keys that have minimum value among candidate dict

        for key, value in cand.items():
            if value == min(cand.values()):
                minIdx.append(key)
        cand.pop(minIdx[0])
        cnt[minIdx[0]] = 0

        cnt[i] += 1
        cand[i] += 1

    else:
        cnt[i] += 1
        cand[i] = cnt[i]

answer = []
for int_key in sorted(cand.keys()):
    answer.append(str(int_key))
print(' '.join(answer))
