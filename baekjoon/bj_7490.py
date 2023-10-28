# baekjoon 7490
# 0 만들기

testcase = int(input())
N = [int(input()) for _ in range(testcase)]

# i: operand (2, ..., N)
# temp: result of the previous step of p, p[:-2] 
# num: result of the expression p
def solution(depth, i, temp, num): 
    global p
    
    if i-1 == depth:
        if num == 0:
            result.append(p)
        return
    
    for j in range(3): # '+', '-', ' '
 
        if j == 0: # '+'
            p = p + '+' + str(i)
            solution(depth, i+1, num, num+i)
    
        elif j == 1: # '-'
            p = p + '-' + str(i)
            solution(depth, i+1, num, num-i)
     
        else: # j == 2: # ' '
            p = p + ' ' + str(i)
            if i == 2:
                solution(depth, i+1, num, temp*10+i)
            elif p[-4] == '-': # i > 2:
                solution(depth, i+1, num, temp - (int(p[-3])*10+i))
            elif p[-4] == '+': # i > 2:
                solution(depth, i+1, num, temp + (int(p[-3])*10+i))
        p = p[:-2] # previous step of p

for i in N:
    operand = [j+1 for j in range(i)] # 1, 2, ..., N
    result = []
    p = '1'
    solution(i, 2, 1, 1)
    
    result = sorted(result)
    for k in range(len(result)):
        print(result[k])
    print()
