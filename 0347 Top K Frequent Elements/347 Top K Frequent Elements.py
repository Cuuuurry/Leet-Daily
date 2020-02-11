from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}

        for num in nums:
            if num not in numCount:
                numCount[num] = -1
            else:
                numCount[num] -= 1

        heap = []
        for key, item in numCount.items():
            heapq.heappush(heap, [item, key])

        result = []
        for i in range(k):
            negFreq, freElement = heapq.heappop(heap)
            result.append(freElement)

        return result
