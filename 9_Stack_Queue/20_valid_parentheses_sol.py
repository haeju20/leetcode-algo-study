class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')':
                if stack and stack.pop() == '(':
                    continue
                else:
                    return False
            elif i == '}':
                if stack and stack.pop() == '{':
                    continue
                else:
                    return False
            else: # i == ']'
                if stack and stack.pop() == '[':
                    continue
                else:
                    return False
        return len(stack) == 0

# class Solution2: # using Dictionary
#     def isValid(self, s: str) -> bool:
#         stack = []
#         dict = {
#             '(': ')',
#             '{': '}',
#             '[': ']',
#         }
#
#         for i in s:
#             if i in dict: # i is key of dict
#                 stack.append(i)
#             elif stack and dict[stack.pop()] == i: # i is value of dict
#                 continue
#             else:
#                 return False
#         return len(stack) == 0
