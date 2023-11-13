#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxprofit(pricess):
    l = 0
    r = 1
    m = 0
    while r < len(pricess):
        
        if (pricess[l] < pricess[r]):
            profit = pricess[r]-pricess[l]
            if profit > m:
                m = profit
        else:
            l = r
        r += 1
    return m
print(maxprofit([7,1,5,0,6,7]))