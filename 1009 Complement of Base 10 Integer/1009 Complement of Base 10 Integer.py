class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if not N: return 1
        n = 0
        while 2 ** n - 1 < N:
            n += 1
        return 2 ** n - 1 - N
