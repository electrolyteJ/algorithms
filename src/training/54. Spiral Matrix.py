'''
54. 螺旋矩阵
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''


class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        ret = []
        r, c = 0, 0
        m, n = len(matrix), len(matrix[0])
        visited = [[False]*n for _ in range(m)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        d_i = 0
        # 时间复杂度O(m*n) 空间复杂度O(m*n)
        for _ in range(m*n):
            ret.append(matrix[r][c])
            visited[r][c] = True
            next_r, next_c = r+dr[d_i], c+dc[d_i]
            if not (0 <= next_r < m and 0 <= next_c < n and not visited[next_r][next_c]):
                d_i = (d_i+1) % 4
            r += dr[d_i]
            c += dc[d_i]

        return ret

    def spiralOrder2(self, matrix):
        if not matrix or not matrix[0]:
            return []
        ret = []
        m, n = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, n-1, 0, m-1
        while left <= right and top <= bottom:
            for c in range(left, right+1):
                ret.append(matrix[top][c])
            for r in range(top+1, bottom+1):
                ret.append(matrix[r][right])
            if left < right and top < bottom:
                for c in range(right-1, left, -1):
                    ret.append(matrix[bottom][c])
                for r in range(bottom, top, -1):
                    ret.append(matrix[r][left])
            left, right, top, bottom = left+1, right-1, top+1, bottom-1
        return ret


if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
    print('1', s.spiralOrder(matrix))
    print('2', s.spiralOrder2(matrix))
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print('1', s.spiralOrder(matrix))
    print('2', s.spiralOrder2(matrix))
