class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracked = dict()
        for i in range(len(nums)):
            need = target - nums[i]
            if need in tracked:
                return [tracked[need], i]
            tracked[nums[i]] = i
        return None

                
        