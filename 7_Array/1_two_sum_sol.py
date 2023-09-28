class Solution: # brute-force
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    result += i, j # return [i, j]
        return result

# class Solution2: # find the result of subtracting a value from target
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             if target - nums[i] in nums[i+1:]:
#                 return [i, nums.index(target - nums[i], i+1, len(nums))]
#                 # return [i, nums[i+1:].index(target - nums[i]) + (i + 1)]
#                 # add (i+1) because it is based on nums[i+1:]

# class Solution3: # using enumerate
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i, num in enumerate(nums):
#             sub = target - num
#             if sub in nums[i+1:]:
#                 return [nums.index(num), nums[i+1:].index(sub)+ (i+1)]

# class Solution4: # find by key the result of subtracting a value from target
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums_map = {}
#         for i, num in enumerate(nums): # replace key and value
#             nums_map[num] = i
#         for i, num in enumerate(nums):
#             if target - num in nums_map and i != nums_map[target - num]:
#                 return [i, nums_map[target - num]]
