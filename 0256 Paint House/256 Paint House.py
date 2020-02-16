from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        chooseRed = 0
        chooseGreen = 0
        chooseBlue = 0
        for red, green, blue in costs:
            chooseRed, chooseGreen, chooseBlue = \
                min(chooseGreen, chooseBlue) + red, \
                min(chooseRed, chooseBlue) + green, \
                min(chooseRed, chooseGreen) + blue

        return min(chooseRed, chooseGreen, chooseBlue)