from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        sumLeftUp = [[0] * (len(mat[0]) + 1) for _ in range(len(mat) + 1)]
        for row in range(len(mat)):
            rowSum = 0
            for col in range(len(mat[0])):
                rowSum += mat[row][col]
                sumLeftUp[row + 1][col + 1] = sumLeftUp[row][col + 1] + rowSum
        print(sumLeftUp)

        maxEdge = min(len(mat[0]), len(mat))

        for edge in range(maxEdge):
            for row in range(1, len(sumLeftUp)):
                flag = False
                for col in range(1, len(sumLeftUp[0])):
                    
                    break

        return


if __name__ == "__main__":
    s = Solution()
    mat = [[1, 2, 5, 7, 11, 14, 16], [2, 4, 10, 14, 22, 28, 32], [3, 6, 15, 21, 33, 42, 48]]
    threshold = 4
    print(s.maxSideLength(mat, threshold))
