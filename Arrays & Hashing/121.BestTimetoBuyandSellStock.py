from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 0      # tracks best day to buy (min price seen)
        high = 1    # iterates as potential sell day
        max_profit = 0
        
        while high < len(prices):
            # if current price <= min seen, update best buy day
            if prices[high] <= prices[low]:
                low = high
            else:
                # calculate profit and keep the max
                max_profit = max(max_profit, prices[high] - prices[low])
            high += 1
            
        return max_profit

# TRICK: Two pointers - low tracks minimum price, high scans forward.
# For any sell day, the best buy day is the minimum before it.
# T(N) = O(n) - single pass
# S(N) = O(1)