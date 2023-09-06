class Solution: # sort a string by sorted()
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)

        for str in strs:
            result[''.join(sorted(str))].append(str) # append to dict

        return list(result.values())
