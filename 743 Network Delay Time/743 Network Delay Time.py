from typing import List
import heapq
import collections


class Solution(object):
    def networkDelayTime(self, times, N, K):
        """pq = [(0, K)]
        dist = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist: continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d + d2, nei))

        return max(dist.values()) if len(dist) == N else -1"""
        graph = collections.defaultdict(list)
        for u, v, time in times:
            graph[u].append([time, v])

        pq = [(0, K)]
        dist = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist: continue
            dist[node] = d
            for time, target in graph[node]:
                if target not in dist:
                    heapq.heappush(pq, (d + time, target))

        return max(dist.values()) if len(dist) == N else -1

if __name__ == "__main__":
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    N = 4
    K = 2
    s = Solution()
    print(s.networkDelayTime(times, N, K))