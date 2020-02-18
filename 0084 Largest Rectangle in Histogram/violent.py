from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        for i in range(len(heights)):
            count = 0
            for j in range(len(heights)):
                if heights[j] < heights[i]:
                    count = 0
                else:
                    count += 1
                result = max(result, count * heights[i])

        return result