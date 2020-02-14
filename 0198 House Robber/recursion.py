from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        recursionDict = {}

        def robEnd(num):
            if num in recursionDict:
                return recursionDict[num]
            if num < 0:
                return 0
            if num == 0:
                return nums[0]

            recursionDict[num] = max(robEnd(num - 2) + nums[num],
                                     robEnd(num - 1))
            return recursionDict[num]

        return robEnd(len(nums) - 1)
