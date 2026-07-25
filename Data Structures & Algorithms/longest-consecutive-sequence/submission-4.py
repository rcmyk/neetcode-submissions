class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        res = 0
        while d:
            current = 1
            n = d.pop()
            for i in range(1, len(nums)):
                if (n+i) in d: current += 1; d.remove(n+i)
                else: break
            for i in range(1, len(nums)):
                if (n-i) in d: current += 1; d.remove(n-i)
                else: break

            res = max(res, current)

        return res
