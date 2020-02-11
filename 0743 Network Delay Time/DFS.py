from typing import List
import heapq
import collections


class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, time in times:
            graph[u].append((time, v))

        dist = {node: float("inf") for node in range(1, N + 1)}

        def dfs(node, elapsed):
            if elapsed >= dist[node]:
                return

            dist[node] = elapsed
            for time, v in sorted(graph[node]):
                dfs(v, elapsed + time)

        dfs(K, 0)
        ans = max(dist.values())

        return ans if ans < float("inf") else -1
