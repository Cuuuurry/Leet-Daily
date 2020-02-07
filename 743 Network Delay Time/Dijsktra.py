from typing import List
import heapq
import collections


class Solution(object):
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, time in times:
            graph[u].append((time, v))

        dist = {node: float("inf") for node in graph}
        seen = [False] * (N + 1)

        dist[K] = 0

        while True:
            



