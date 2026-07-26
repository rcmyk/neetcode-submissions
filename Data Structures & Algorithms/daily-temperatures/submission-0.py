class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        res = [0] * n

        i = 0
        while i < n:
            j = i + 1
            while j < n and temps[j] <= temps[i]:
                j += 1
            res[i] = 0 if j >= n else j - i
            i += 1

        return res