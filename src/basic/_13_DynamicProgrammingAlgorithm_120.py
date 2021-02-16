'''
120. 三角形最小路径和
给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

 

示例 1：

输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11
解释：如下面简图所示：
   2
  3 4
 6 5 7
4 1 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
示例 2：

输入：triangle = [[-10]]
输出：-10
 

提示：

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104

进阶：

你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？
'''


class Solution:
    def minimumTotal1(self, triangle) -> int:  # dp
        if not triangle:
            return 0
        res = triangle[-1].copy()
        #时间复杂度为O(m*n)
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1])+triangle[i][j]
        return res[0]

    def minimumTotal2(self, triangle) -> int:  # 递归+记忆化
        def dfs(triangle, mem, row, col):
            if row == len(triangle)-1:
                return triangle[row][col]

            if mem[row][col]:
                return mem[row][col]

            down = dfs(triangle, mem, row+1, col)
            down_right = dfs(triangle, mem, row+1, col+1)
            mem[row][col] = min(down, down_right) + triangle[row][col]
            return mem[row][col]

        if not triangle:
            return 0
        # mem = [[None]*len(triangle)] * (len(triangle)) 有问题数组内的数组是同一个对象
        mem = [[None for _ in range(len(triangle))]
               for _ in range(len(triangle)-1)]
        r = dfs(triangle, mem, 0, 0)
        return r


if __name__ == '__main__':
    s = Solution()
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print('1', s.minimumTotal1(triangle))
    print('2', s.minimumTotal2(triangle))
    triangle = [[-10]]
    print('1', s.minimumTotal1(triangle))
    print('2', s.minimumTotal2(triangle))
