#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        sell = 0
        profit = 0
        buy_day = 1
        sell_day = 0

        for i in range(1, len(prices)):
            if prices[i] - buy > profit:
                profit = prices[i] - buy
                sell = prices[i]
                sell_day = i + 1

            if prices[i] < buy:
                if i != len(prices) -1:
                    buy = prices[i]
                    buy_day = i + 1
        
        # if buy_day > sell_day:
        #     print(f"No Transactions are done!")
        # else:
        #     print(f"Buy on day: {buy_day}\nSell on day: {sell_day}")

        return profit
    
# @lc code=end

