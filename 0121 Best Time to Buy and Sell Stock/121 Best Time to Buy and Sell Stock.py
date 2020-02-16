from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n != 0:
            # store the minimum price
            min_price = prices[0]
            # store the maximum profit at the time
            max_profit = 0
            # store pointer point to the temporary max profit
            sell_date = 0
            for i in range(n):
                # update the temporary fit
                temp_profit = prices[i] - min_price
                # update the max profit and sell date
                if max_profit < temp_profit:
                    selldate = i
                    max_profit = temp_profit
                # update minimum price
                if min_price > prices[i]:
                    min_price = prices[i]
            return max_profit
        else:
            return 0
