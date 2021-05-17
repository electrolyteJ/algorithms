'''
309. 最佳买卖股票时机含冷冻期
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
'''
class Solution:
    #cool down
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        profit = [[[0 for _ in range(2)] for _ in range(2)]
                  for _ in range(len(prices))]
        # i天数， cool down:0,1，k是否有股票0，1
        profit[0][0][0], profit[0][0][1] = 0, -prices[0]
        profit[0][1][0], profit[0][1][1] = float('-inf'), float('-inf')
        ret =0
        for i in range(1,len(prices)):
            profit[i][0][0] = max(
                profit[i-1][0][0], profit[i-1][1][0])
            profit[i][0][1] = max(profit[i-1][0][1], profit[i-1][0][0]-prices[i])
            profit[i][1][0] = profit[i-1][0][1]+prices[i]
            ret = max(ret, profit[i][0][0], profit[i][0][1], profit[i][1][0])
        return ret
if __name__ =='__main__':
    s = Solution()
    prices = [1,2,3,0,2]
    print('1', s.maxProfit(prices))  # 3
