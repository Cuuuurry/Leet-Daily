from typing import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2: return []
        heap = []
        for i in range(min(len(nums1), k)):
            for j in range(min(len(nums2), k)):
                num1, num2 = nums1[i], nums2[j]
                heapq.heappush(heap, (num1 + num2, num1, num2))

        result = []
        for i in range(min(len(heap), k)):
            tmpSum, num1, num2 = heapq.heappop(heap)
            result.append([num1, num2])

        return result
