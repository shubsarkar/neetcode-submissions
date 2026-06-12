class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # what we need to figure out here is the figuring out the lowest followed by the highest price
        # [7,1,5,3,6,4]

        minPrice = prices[0]
        maxProfit = 0

        for item in prices:
            if item < minPrice:
                minPrice = item

            if item - minPrice > maxProfit:
                maxProfit = item - minPrice
                print (maxProfit)
        return maxProfit