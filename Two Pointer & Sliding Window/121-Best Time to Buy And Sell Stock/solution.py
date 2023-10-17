class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        l = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < l:
                l = prices[i]
            elif prices[i] - l > ans:
                ans = prices[i] - l
        return ans
