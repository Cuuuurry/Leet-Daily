from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = {"-2": nums[0], "-1": max(nums[0], nums[1]), "0": 0}
        dp["0"] = dp["-1"]
        for i in range(2, len(nums)):
            dp["0"] = max(dp["-2"] + nums[i], dp["-1"])
            dp["-2"], dp["-1"] = dp["-1"], dp["0"]

        return dp["0"]