from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = heapq.nlargest(k, nums)
        heapq.heapify(heap)
        return heapq.heappop(heap)