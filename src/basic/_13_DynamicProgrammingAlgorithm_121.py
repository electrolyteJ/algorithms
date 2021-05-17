'''
121. 买卖股票的最佳时机
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
提示：
1 <= prices.length <= 105
0 <= prices[i] <= 104
'''
class Solution:
    # 最多交易一次
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        ret = 0
        profit = [[0 for i in range(3)] for i in range(len(prices))]
        # 没有股票         买入股票       卖出股票
        profit[0][0], profit[0][1], profit[0][2] = 0, -prices[0], 0
        for i in range(1, len(prices)):
            profit[i][0] = profit[i-1][0]
            profit[i][1] = max(profit[i-1][1], profit[i-1][0]-prices[i])
            profit[i][2] = profit[i-1][1] + prices[i]
            ret = max(ret, profit[i][0], profit[i][1], profit[i][2])
            # 如果为1的话说明手上游没有出售的股票，正常是不会考虑这个的，最后都会将股票卖出，所以可以去掉 profit[i][1],为了工整也可以加入
            # ret = max(ret, profit[i][0], profit[i][2])
        return ret

if __name__ == '__main__':
    s = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print('1', s.maxProfit(prices))
    prices = [7, 6, 4, 3, 1]
    print('1', s.maxProfit(prices))
