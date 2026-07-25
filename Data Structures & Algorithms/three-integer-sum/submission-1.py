class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)
        nums.sort()
        prev = {}
        seen = set()
        for i in range(0, N):
            for j in range(i + 1, N):
                need = 0 - nums[i] - nums[j]
                ni = prev[need] if need in prev else -1
                
                if ni == -1:
                    continue

                if ni != -1 and ni != i and ni != j:
                    if (nums[ni], nums[i], nums[j]) in seen:
                        continue
                    res.append([nums[ni], nums[i], nums[j]])
                    seen.add((nums[ni], nums[i], nums[j]))
            prev[nums[i]] = i
                
        return res
