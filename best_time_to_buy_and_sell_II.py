def maxProfit(prices) -> int:
    max_profit = 0
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            # print(prices[i])
            max_profit = max_profit + ( prices[i] - prices[i-1] )
    return max_profit


price_list = [7,1,5,3,6,4]
print(maxProfit(price_list))


