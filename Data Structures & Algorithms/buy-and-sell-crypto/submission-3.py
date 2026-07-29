class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        l=0
        r=len(prices)-1
        while l+1<=r:
            np=prices[l+1:r+1]
            if prices[l]>max(np):
                l+=1
            else:
                new_profit=max(np) -prices[l]  
                profit=max(profit,new_profit)
                l=l+1
        return profit