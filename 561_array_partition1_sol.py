class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0
        nums.sort()
        for i, n in enumerate(nums):
            if i % 2 == 0: # the even-numbered
                result += n
        return result

# class Solution2:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         result = 0
#         asc = sorted(nums)
#         for i in range(0, len(asc), 2):
#             result += asc[i]
#         return result

# class Solution3:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         return sum(sorted(nums)[::2]) # jump by 2
