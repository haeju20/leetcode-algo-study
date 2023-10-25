# baekjoon 1038
# 감소하는 수

N = int(input())
nums = []

def solution(depth, digit, num):
    if depth == digit:
        nums.append(int(num))
       
        if len(nums) > N:
            print(nums[N])
            exit()
        return
   
    for i in range(0, int(num[0])):
        if i < int(num[-1]): # desc
            num += str(i)
            solution(depth+1, digit, num)
            num = num[:-1]
    
for digit in range(1, 11): # digit 1, 2, ..., 10(9876543210)
    if digit == 1:
        for i in range(0, 10):
            nums.append(i)
            
    else: # digit > 1:    
        for num in range(1, 10):
            solution(1, digit, str(num))

print(-1) # cannot find nums[N]
