'''
63. 不同路径 II
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。
示例 1：
输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
示例 2：

输入：obstacleGrid = [[0,1],[0,0]]
输出：1

提示：

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] 为 0 或 1
'''

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        #时间复杂度O(mn) 空间复杂度O(mn)
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if i > 0:
                        dp[i][j] = dp[i-1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j-1]

        return dp[-1][-1]

    # dp优化滚动数组
    def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp =[0]*n
        #时间复杂度O(mn) 空间复杂度O(n)
        dp[0] = 1 if obstacleGrid[0][0]==0 else 0
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==0:
                    if j-1 >=0 and obstacleGrid[i][j-1] ==0:
                        dp[j] +=dp[j-1]
                else:
                    dp[j]=0
        return dp[-1]
if __name__ == '__main__':
    s = Solution()
    obstacleGrid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]]
    print('1', s.uniquePathsWithObstacles(obstacleGrid))
    print('2', s.uniquePathsWithObstacles2(obstacleGrid))
    obstacleGrid = [
        [1, 0]
    ]
    print('1', s.uniquePathsWithObstacles(obstacleGrid))
    print('2', s.uniquePathsWithObstacles2(obstacleGrid))
