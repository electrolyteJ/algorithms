'''
48. 旋转图像
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]
示例 2：
输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
示例 3：
输入：matrix = [[1]]
输出：[[1]]
示例 4：
输入：matrix = [[1,2],[3,4]]
输出：[[3,1],[4,2]]
提示：
matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

'''
class Solution:

    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n < 2:
            return
        left, top, right, bottom = 0, 0, n-1, n-1
        #时间复杂度O(n*n)
        while n >= 2:
            for i in range(n-1):  # 0 1 2
                matrix[top][left+i], matrix[top+i][right], matrix[bottom][right -
                                                                          i], matrix[bottom-i][left] = matrix[bottom-i][left], matrix[top][left+i], matrix[top+i][right], matrix[bottom][right -
                                                                                                                                                                                         i]
            n -= 2
            left, top, right, bottom = left+1, top+1, right-1, bottom-1


if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print('1', s.rotate(matrix), matrix)
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print('1', s.rotate(matrix), matrix)
    matrix = [[1]]
    print('1', s.rotate(matrix), matrix)
    matrix = [
        [1, 2],
        [3, 4]
    ]
    print('1', s.rotate(matrix), matrix)
