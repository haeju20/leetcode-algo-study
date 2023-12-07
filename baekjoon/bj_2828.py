# baekjoon 2828
# 사과 담기 게임

N, M = map(int, input().split())
J = int(input())
apple = [ int(input()) for _ in range(J) ]

loc = 1 # basket reaches from loc to loc+(M-1)
dis = 0 # minimum value of distance

for i in range(J):
    # if the apple falls into the basket
    if loc <= apple[i] <= loc+(M-1):
        continue
    
    if loc < apple[i]: # move to right
        dis += abs(loc - apple[i]) - (M - 1) # update the travel distance 
        loc += abs(loc - apple[i]) - (M - 1) # update the current location of basket
    else: # loc > apple[i]: move to left
        dis += abs(loc - apple[i])
        loc -= abs(loc - apple[i])

print(dis)
