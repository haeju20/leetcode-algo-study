# baekjoon 15658
# 연산자 끼워넣기 (2)

# same code with 14888 - 연산자 끼워넣기 
# the number of operator >= N-1
# but the func finishes if i == N (N operators) in this case too

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
