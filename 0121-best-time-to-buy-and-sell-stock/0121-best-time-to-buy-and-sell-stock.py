class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxprofit = 0

        for price in prices[1:]:
            maxprofit = max(maxprofit,price-minprice)
            minprice = min(minprice,price)

        return maxprofit    

        