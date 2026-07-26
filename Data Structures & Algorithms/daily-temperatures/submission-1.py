class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        res = [0] * n

        stack = []
        for i, temp in enumerate(temps):
            while stack and temp > temps[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)

        return res