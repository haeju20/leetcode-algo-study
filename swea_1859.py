# fail (runtime error)
# N = int(input())
# p = list(map(int, input().split()))
# print(p)
# b = []
# cnt = 0

# for i in range(N-1): 
#     if i == N-2 and p[i] < p[i+1]:
#         b.append(p[i])
#         for j in range(len(b)):
#             cnt += p[i+1] - b[j]
#         b = []
#         continue

#     if p[i] > p[i+1]:
#         for j in range(len(b)):
#             cnt += p[i] - b[j]
#         b = []
        
#     if p[i] <= p[i+1]:
#         b.append(p[i])
        
# print(cnt)
