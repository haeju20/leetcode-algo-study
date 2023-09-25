class Solution: # using Hash Table
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        cnt = {}
        # count the number of stones with comparison
        for s in stones:
            if s not in cnt:
                cnt[s] = 1
            else:
                cnt[s] += 1

        for j in jewels:
            if j in cnt:
                result += cnt[j]

        return result

# class Solution: # using defaultdict
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         result = 0
#         cnt = collections.defaultdict(int)
#         # count the number of stones
#         for s in stones:
#             cnt[s] += 1
#
#         for j in jewels:
#             result += cnt[j]
#
#         return result

# class Solution: # using Counter
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         result = 0
#         cnt = collections.Counter(stones)
#         key = list(cnt.keys())
#
#         for i in jewels:
#             if i in key:
#                 result += cnt[i]
#         return result
