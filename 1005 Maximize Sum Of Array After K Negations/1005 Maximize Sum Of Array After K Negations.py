from typing import List
import heapq


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        if not A: return 0
        heapq.heapify(A)
        for i in range(K):
            smallest = heapq.heappop(A)
            smallest = -smallest
            heapq.heappush(A, smallest)
        return sum(A)