from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        ans = []
        for i in range(len(intervals)):
            if i == 0:
                ans.append(intervals[i])
            else:
                if ans[-1][1] >= intervals[i][0]:
                    intervalToBeChanged = ans.pop()
                    intervalToBeChanged[1] = max(intervals[i][1], intervalToBeChanged[1])
                    ans.append(intervalToBeChanged)
                else:
                    ans.append(intervals[i])

        return ans
