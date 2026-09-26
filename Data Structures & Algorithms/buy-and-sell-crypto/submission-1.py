class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0 
        left = 0
        right = 1

        while right <= (len(prices) - 1):
            if prices[left] >= prices[right]:
                left = right
                right += 1
            else:
                maximum = max(maximum, prices[right] - prices[left])
                right += 1

        return maximum


        