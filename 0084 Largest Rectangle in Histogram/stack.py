from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        heights = [0] + heights + [0]
        stack = []
        candidates = [0]
        for i in range(len(heights)):
            # print(stack)
            while stack and stack[-1][0] > heights[i]:
                candidates.append(stack[-1][0] * (i - stack[-2][1] - 1))
                stack.pop()
            stack.append((heights[i], i))

        return max(candidates)