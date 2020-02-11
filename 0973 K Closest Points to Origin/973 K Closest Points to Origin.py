from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not K or not points: return []
        heapPoints = []
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            heapq.heappush(heapPoints, [dist, point])

        KClosest = []
        for i in range(K):
            heapPoint = heapq.heappop(heapPoints)
            dist, point = heapPoint
            KClosest.append(point)

        return KClosest