'''
322. 零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
你可以认为每种硬币的数量是无限的。
示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
示例 2：
输入：coins = [2], amount = 3
输出：-1
示例 3：
输入：coins = [1], amount = 0
输出：0
示例 4：
输入：coins = [1], amount = 1
输出：1
示例 5：
输入：coins = [1], amount = 2
输出：2
提示：
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
'''
class Solution:
    def coinChange1(self, amount: int, coins) -> int:#记忆化
        dp = [-1]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for coin in coins:
                if i >=coin:
                    # dp[i] = min(dp[i],dp[i-coin]+1)
                    dp[i] = dp[coin]+dp[i-coin]
        return  dp[amount]
    def coinChange2(self, amount: int, coins) -> int:#dp
        # dp[i] 凑成到金额i的最少硬币个数
        # dp[i] = min(dp[i-coins[j]])+1
        # dp = [amount+1]*(amount+1)
        dp = [amount+1]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for coin in coins:
                if i >=coin:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        return  -1 if dp[amount] >amount else dp[amount]

if __name__ == '__main__':
    s = Solution()
    amount =11
    coins = [1, 2, 5]
    print('1', s.coinChange1(amount, coins))
    print('2', s.coinChange2(amount, coins))
    amount = 3
    coins = [2]
    print('1', s.coinChange1(amount, coins))
    print('2', s.coinChange2(amount, coins))
    coins = [1]; amount = 0
    print('1', s.coinChange1(amount, coins))
    print('2', s.coinChange2(amount, coins))
    coins = [1]; amount = 1
    print('1', s.coinChange1(amount, coins))
    print('2', s.coinChange2(amount, coins))
    coins = [1]; amount = 2
    print('1', s.coinChange1(amount, coins))
    print('2', s.coinChange2(amount, coins))
