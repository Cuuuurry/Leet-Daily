from typing import List
import heapq
import collections


class Solution(object):
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, time in times:
            graph[u].append((time, v))

        for key in graph:
            print(f"key is {key}")

        dist = {node: float("inf") for node in range(1, N+1)}
        seen = [False] * (N + 1)

        dist[K] = 0

        while True:
            can_node = -1
            can_dist = float("inf")
            for i in range(1, N + 1):
                if not seen[i] and dist[i] < can_dist:
                    can_dist = dist[i]
                    can_node = i

            if can_node < 0: break

            seen[can_node] = True
            for time, v in graph[can_node]:
                dist[v] = min(dist[v], dist[can_node] + time)

        ans = max(dist.values())
        return ans if ans < float("inf") else -1

if __name__ == "__main__":
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    N = 4
    K = 2
    s = Solution()
    print(s.networkDelayTime(times, N, K))