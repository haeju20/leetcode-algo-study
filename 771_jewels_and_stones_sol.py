class Solution: # using Counter
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        cnt = collections.Counter(stones)
        key = list(cnt.keys())

        for i in jewels:
            if i in key:
                result += cnt[i]
        return result
