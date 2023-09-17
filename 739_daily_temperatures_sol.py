class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                idx = stack.pop()
                answer[idx] = i - idx # difference of indexs
            stack.append(i) # append index of temperature

        return answer
