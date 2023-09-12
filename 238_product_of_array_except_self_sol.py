class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        p = 1
        for i in range(0, len(nums)): # from left
            answer.append(p)
            p *= nums[i]
        p = 1
        for j in range(len(nums) - 1, -1, -1): # from right
            answer[j] *= p
            p *= nums[j]
        return answer
