class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min = prices[0]
        profit = 0
        n = len(prices)
        for i in range(n):
            if prices[i] < min:
                min = prices[i]
            elif prices[i] - min > profit:
                profit = prices[i] - min

        return profit
