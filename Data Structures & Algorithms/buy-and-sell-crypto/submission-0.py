class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                r = max(r, prices[j] - prices[i])
        return r