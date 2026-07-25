class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroIdx = -1
        mult = 1
        for i, n in enumerate(nums):
            if n == 0:
                if zeroIdx != -1: # double zero
                    return [0] * len(nums)
                zeroIdx = i
            else:
                mult *= n
        if zeroIdx >= 0: # one zero
            out = [0] * len(nums)
            out[zeroIdx] = mult
            return out

        out = [mult] * len(nums)
        for i, n in enumerate(nums):
            out[i] //= n
        return out
        