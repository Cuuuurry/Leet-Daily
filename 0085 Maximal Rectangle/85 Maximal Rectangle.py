from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        maxDp = 0

        for start_row in range(m):
            for start_col in range(n):
                if matrix[start_row][start_col] == "1":
                    candidate = []
                    candidateRow = []
                    for end_row in range(start_row, m):
                        count = 0
                        if matrix[end_row][start_col] == "0":
                            break
                        for end_col in range(start_col, n):
                            if matrix[end_row][end_col] == "1":
                                count += 1
                            else:
                                break
                        candidateRow.append(count)

                        # print(f"the candidate num for this row {end_row} of {start_row} {start_col} is {candidateRow}")
                        candidate.append(min(candidateRow) * (end_row - start_row + 1))
                    # print(f"The candidate for start coordinate {start_row} {start_col} is {candidate}")
                    dp[start_row][start_col] = max(candidate)
                    maxDp = max(dp[start_row][start_col], maxDp)

        return maxDp


if __name__ == "__main__":
    input_value = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    s = Solution()
    print(s.maximalRectangle(input_value))
