class Solution3: # 문자열 뒤집기
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]

# class Solution2:
#     def isPalindrome(self, s: str) -> bool:
#         test = []
#         for i in s:
#             if i.isalnum():
#                 test.append(i.lower())
#         print(test)
#         for i in range(0, len(test)//2):
#             if test[i] != test[-(i+1)]:
#                 return False
#         return True

# class Solution3: # 데크를 활용하여 O(n) -> O(1)
#     def isPalindrome(self, s: str) -> bool:
#         test: Deque = collections.deque()
#
#         for i in s:
#             if i.isalnum():
#                 test.append(i.lower())
#
#         while len(test) > 1:
#             if test.popleft() != test.pop():
#                 return False
#         return True
