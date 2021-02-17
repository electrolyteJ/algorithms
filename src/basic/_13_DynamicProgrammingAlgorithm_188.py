'''
188. 买卖股票的最佳时机 IV
给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。



示例 1：

输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2：

输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。


提示：

0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000

'''


class Solution:
    # 最多交易k次
    def maxProfit(self, k: int, prices) -> int:
        # 时间复杂度O(n*k)空间复杂度O(n*k)
        if not prices or k == 0:
            return 0
        profit = [[[0 for _ in range(2)] for _ in range(k+1)]
                  for _ in range(len(prices))]
        # i天数，j交易次数，k是否持股
        profit[0][0][0], profit[0][0][1] = 0, -prices[0]
        ret = 0
        for kk in range(1, k+1):
            profit[0][kk][0], profit[0][kk][1] = float('-inf'), float('-inf')
        for i in range(1, len(prices)):
            profit[i][0][0] = profit[i-1][0][0]
            profit[i][0][1] = max(profit[i-1][0][1], profit[i-1][0][0]-prices[i])
            for kk in range(1, k+1):
                profit[i][kk][0] = max(profit[i-1][kk][0], profit[i-1][kk-1][1]+prices[i])
                profit[i][kk][1] = max(profit[i-1][kk][1], profit[i-1][kk][0]-prices[i])
                ret = max(ret, profit[i][0][0], profit[i][0][1],profit[i][kk][0])
        return ret


if __name__ == '__main__':
    s = Solution()
    prices = [2, 4, 1]
    k = 2
    print('1', s.maxProfit(k, prices))  # 2
    prices = [3, 2, 6, 5, 0, 3]
    k = 2
    print('1', s.maxProfit(k, prices))  # 7
