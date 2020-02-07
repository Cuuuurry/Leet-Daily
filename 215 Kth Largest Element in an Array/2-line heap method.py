from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        find the Kth largest number in a queue
        :param nums:
        :param k:
        :return:
        """
        heap = heapq.nlargest(k, nums)
        heapq.heapify(heap)
        return heapq.heappop(heap)