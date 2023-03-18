'''
Leetcode: 121. Best Time to Buy and Sell Stock
https://www.educative.io/courses/grokking-coding-interview-patterns-python/B813QM8R482

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

from typing import List


def maxProfit(prices: List[int]) -> int:
    left = 0
    right = 1
    max_profit = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            curr_profit = prices[right] - prices[left]
            max_profit = max(max_profit, curr_profit)
            right += 1
        else:
            left += 1
            right += 1
    
    return max_profit


def main():
    list_prices = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],
        [8, 2, 4, 13, 10],
        [10, 4, 11, 1, 5],
        [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9],
        [1, 2]
    ]
    
    for i in range(len(list_prices)):
        print(i + 1, '. \t Input String: ', list_prices[i], sep='')
        print('\t The maximum profit you can achieve is: ',
                (maxProfit(list_prices[i])))
        print('-' * 55)


if __name__ == '__main__':
    main()

'''
TC -> O(n) 
SC -> O(1)
'''