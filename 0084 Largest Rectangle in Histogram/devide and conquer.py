from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        # find the minimum to divide
        for breakpoint in range(len(heights)):
            if heights[breakpoint] == min(heights):
                break
        middleArea = heights[breakpoint] * len(heights)
        leftArea, rightArea = 0, 0

        # conquer each part
        if breakpoint >= 1:
            leftArea = self.largestRectangleArea(heights[:breakpoint])
        if breakpoint < len(heights) - 1:
            rightArea = self.largestRectangleArea(heights[breakpoint + 1:])

        # print(f"For {heights}, we have {leftArea}, {middleArea}, {rightArea}")

        return max(leftArea, middleArea, rightArea)