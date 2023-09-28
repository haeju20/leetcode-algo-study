class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        min_price = prices[0]
        for i in range(0, len(prices)):
            # i=0, profit=0
            # calculate current price - min(so far)
            profit.append(prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return max(profit)

# class Solution2:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
#         min_price = sys.maxsize # max value in system
#         # update min and profit 
#         for i in prices:
#             min_price = min(min_price, i)
#             profit = max(profit, i - min_price)
#         return profit
