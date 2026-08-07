class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minv = 100
        
        for i in prices:
            minv = min(minv, i)
            profit = max(profit, i-minv)

        return profit 


        