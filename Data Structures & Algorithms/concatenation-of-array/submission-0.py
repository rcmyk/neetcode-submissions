class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        out = []
        out.extend(nums)
        out.extend(nums)
        return out