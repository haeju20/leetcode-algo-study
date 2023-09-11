class Solution: # two pointer
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            # skip the positive duplicate value i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # narrow the range, calculate sum
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else: # sum = 0
                    result.append([nums[i], nums[left], nums[right]])
                    # skip the duplicate value
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # move pointers together because the sum = 0
                    left += 1
                    right -= 1
        return result

# time limit exceeded when using brute-force
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         result, i_re, j_re = [], [], []
#         for i in nums:
#             nums_copy = nums.copy()
#             nums_copy.remove(i)
#             i_re = nums_copy.copy()
#             for j in i_re:
#                 nums_copy = i_re.copy()
#                 nums_copy.remove(j)
#                 j_re = nums_copy.copy()
#                 if -(i+j) in t2:
#                     result.append(sorted([i, j, -(i+j)]))
#         return list(set(map(tuple, result)))
