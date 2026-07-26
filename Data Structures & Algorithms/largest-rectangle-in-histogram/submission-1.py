class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # (index, height)

        for i, h in enumerate(heights):
            starting = i
            # if h >= stack[-1].height, it's okay to push and move on
            # else: pop and calculate max
            while stack and h < stack[-1][1]:
                idx, height = stack.pop()
                maxArea = max(maxArea, (i - idx) * height)
                starting = idx

            # index = starting, because we are extending to the last one on the stack
            stack.append((starting, h))

        while stack:
            i, h = stack.pop()
            maxArea = max(maxArea, (len(heights) - i) * h)

        return maxArea
