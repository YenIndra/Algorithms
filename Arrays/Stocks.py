def maxProfit(self, prices: List[int]) -> int:
        profit  = 0
        left = 0 
        right = 1 
        while right < len(prices):
            currentProfit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                profit =max(currentProfit,profit)
            else:
                left = right
            right += 1
        return profit
        
