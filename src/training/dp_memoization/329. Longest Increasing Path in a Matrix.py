'''
329. 矩阵中的最长递增路径
给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。
对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。
示例 1：
输入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
输出：4 
解释：最长递增路径为 [1, 2, 6, 9]。
示例 2：
输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
输出：4 
解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
示例 3：
输入：matrix = [[1]]
输出：1 
提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
'''
class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]
        max_len = 0

        def dfs(r, c):
            if memo[r][c] != 0:
                return memo[r][c]
            memo[r][c] = 1
            for k in range(4):
                nr, nc = r+dr[k], c+dc[k]
                if 0 <= nr < m and 0 <= nc < n and matrix[r][c] < matrix[nr][nc]:
                    memo[r][c] = max(memo[r][c], dfs(nr, nc)+1)
            return memo[r][c]

        m = len(matrix)
        n = len(matrix[0])
        # 时间复杂度O(m*n) 空间复杂度O(mn)
        memo = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                max_len = max(max_len, dfs(i, j))
        return max_len

    def longestIncreasingPath2(self, matrix) -> int:  # dp
        #1.拓扑排序
        #2.dp
        m,n = len(matrix),len(matrix[0])

        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]
        dp = [[0]*n for _ in range(m)]
        dp[0][0]=1
        max_len=0
        for i in range(m):
            for j in range(n):
                for k in range(4):
                    nr, nc = i+dr[k], j+dc[k]
                    if 0 <= nr < m and 0 <= nc < n and matrix[i][j] < matrix[nr][nc]:
                            dp[i][j] = max(dp[i][j], dp[nr][nc]+1)
                max_len = max(max_len, dp[i][j])
        return max_len


if __name__ == '__main__':
    s = Solution()
    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    print('1', s.longestIncreasingPath(matrix))  # 4
    print('2', s.longestIncreasingPath2(matrix))  # 4
    matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
    print('1', s.longestIncreasingPath(matrix))  # 4
    print('2', s.longestIncreasingPath2(matrix))
    matrix = [[1]]
    print('1', s.longestIncreasingPath(matrix))  # 1
    print('2', s.longestIncreasingPath2(matrix))
    matrix = [[1, 2]]
    print('1', s.longestIncreasingPath(matrix))
    print('2', s.longestIncreasingPath2(matrix))
