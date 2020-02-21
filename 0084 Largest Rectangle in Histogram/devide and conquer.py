from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # should not convey the entire list, that may explode the RAM

        def maxArea(start, end):
            if start >= end:
                return 0
            miniInList = min(heights[start: end])
            for breakpoint in range(start, end):
                if heights[breakpoint] == miniInList:
                    break
            middleArea = heights[breakpoint] * (end - start)
            leftArea, rightArea = 0, 0
            if breakpoint > start:
                leftArea = maxArea(start, breakpoint)
            if breakpoint < end - 1:
                rightArea = maxArea(breakpoint + 1, end)
            return max(leftArea, middleArea, rightArea)

        return maxArea(0, len(heights))