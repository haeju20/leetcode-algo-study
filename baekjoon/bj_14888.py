# baekjoon 14888
# 연산자 끼워넣기

N = int(input()) 
nums = list(map(int, input().split())) 
add, sub, mul, div = map(int, input().split())

maxVal = int(-1e9)
minVal = int(1e9)
      
def solution(i, num):
    global add, sub, mul, div, maxVal, minVal
    
    if i == N: 
        maxVal = max(maxVal, num)
        minVal = min(minVal, num)
        return

  # not if-elif (those cases can be occured simultaneously)
    if add > 0:
        add -= 1
        solution(i+1, num + nums[i])
        add += 1
    if sub > 0:
        sub -= 1
        solution(i+1, num - nums[i])
        sub += 1
    if mul > 0:
        mul -= 1
        solution(i+1, num * nums[i])
        mul += 1
    if div > 0:
        div -= 1
        solution(i+1, int(num / nums[i]))
        div += 1
    
solution(1, nums[0]) 
print(maxVal)
print(minVal)

## 아래의 풀이는 시간초과
# N = int(input()) # length(the numbers) of operand
# operand = list(map(int, input().split())) 
# operator = list(map(int, input().split())) 

# p = [] # list of operators

# for i in range(len(operator)):
#     if operator[i] > 0:
#         for _ in range(operator[i]):
#             p.append(i)
       
# s = [] # order of operators from each expression
# visited = [False] * len(p)

# maxVal = int(-1e9)
# minVal = int(1e9)

# def calculate(s): # calculate
#     num = operand[0]
    
#     for i in range(len(p)):
#         if s[i] == 0: # +
#             num += operand[i+1]
#         elif s[i] == 1: # -
#             num -= operand[i+1]
#         elif s[i] == 2: # x
#             num *= operand[i+1]
#         elif s[i] == 3 and num > 0: # // of positive integer
#             num //= operand[i+1]
#         else: # // of negative integer
#             num = -(abs(num) // operand[i+1])
#     return num # result of calculate
      
# def solution(M):
#     global s, maxVal, minVal
    
#     if M == 0: 
#         result = calculate(s)
#         # after calculating each case
#         maxVal = max(maxVal, result)
#         minVal = min(minVal, result)
#         return
    
#     # permutation of operator (with repetition)
#     for i in range(len(p)):
#         if visited[i] == False:
#             s.append(p[i])
#             visited[i] = True
#             solution(M-1)
#             visited[i] = False
#             s = s[:-1]
    
# solution(len(p)) # the numbers of operators
# print(maxVal)
# print(minVal)
