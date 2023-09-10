class Solution:
    def longestPalindrome(self, s: str) -> str:
        str = s
        l = len(s)
        while l > 0:
            if str == str[::-1]:
                return str
            else:
                l -= 1
                for i in range(len(s)-l+1):
                    substr = str[i:i+l]
                    if substr == substr[::-1]:
                        return substr

# class Solution: # two pointer expansion
#     def longestPalindrome(self, s: str) -> str:
#         def expand(left: int, right: int) -> str:
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right +=1
#             return s[left + 1:right]
#
#         if len(s) < 2 or s == s[::-1]: # palindrome
#             return s
#
#         result = ''
#         for i in range(len(s) - 1): # sliding window moves right
#             result = max(result, expand(i, i+1), expand(i, i+2), key= len)
#         return result
