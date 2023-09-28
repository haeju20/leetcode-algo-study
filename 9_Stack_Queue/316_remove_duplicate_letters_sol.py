class Solution: # using Stack
    def removeDuplicateLetters(self, s: str) -> str:
        counter = collections.Counter(s)
        visited = set()
        stack = []

        for i in s:
            counter[i] -= 1
            if i in visited:
                continue
            # stack is not empty
            # i is smaller than stack[-1] in lexicographical order
            # stack[-1] will appears at least once more in the future
            while stack and i < stack[-1] and counter[stack[-1]] > 0:
                visited.remove(stack.pop())
            stack.append(i)
            visited.add(i)
            
        return ''.join(stack)

# class Solution: # using Recursion
#     def removeDuplicateLetters(self, s: str) -> str:
#         for i in sorted(set(s)): # remove duplicate letters and sort
#             r = s[s.index(i):]
#             if set(s) == set(r): # if it can be separated based on i
#                 return i + self.removeDuplicateLetters(r.replace(i, ''))
#         return ''
