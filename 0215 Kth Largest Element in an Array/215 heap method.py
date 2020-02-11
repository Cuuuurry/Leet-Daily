from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        :param nums: List[int
        :param k: int
        :return: int
        """
        # null check
        if not nums:
            return 0

        # heapify to get a min heap
        heapq.heapify(nums)

        # pop n-k times to find the kth largest number
        while len(nums) > k:
            heapq.heappop(nums)
            
        return nums[0]
