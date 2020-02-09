import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if not n: return 0
        dp = [ 0 for _ in range(n) ]
        num = 1
        dp[0] = num
        primes = {2:0, 3:0, 5:0}
        count = 1
        while count < n:
            tmpHeap = []
            for prime, index in primes.items():
                heapq.heappush(tmpHeap, (dp[index]*prime, prime))
            preNum = float("inf")
            while tmpHeap:
                thisNum, prime = heapq.heappop(tmpHeap)
                if thisNum > dp[count-1] and thisNum <= preNum:
                    primes[prime] += 1
                    preNum = thisNum
                else:
                    break
            dp[count] = preNum
            count += 1
        return dp[-1]