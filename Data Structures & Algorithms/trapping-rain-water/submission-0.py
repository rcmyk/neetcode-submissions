class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        leftMax = height[l]
        rightMax = height[r]

        total = 0

        while l < r:
            if height[l] < height[r]:
                leftMax = max(leftMax, height[l])
                total += leftMax - height[l]
                l += 1
            else:
                rightMax = max(rightMax, height[r])
                total += rightMax - height[r]
                r -= 1
        return total
