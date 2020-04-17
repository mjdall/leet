def max_profit(prices):
        """
        Max profit buying/selling stock.
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
            return 0

        profit = 0

        for i in range(0, len(prices)-1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]

        return profit
