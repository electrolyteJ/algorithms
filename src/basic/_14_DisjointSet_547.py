'''
547. 省份数量
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。
返回矩阵中 省份 的数量。
示例 1：
输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2
示例 2：
输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
输出：3
提示：
1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] 为 1 或 0
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
'''
class UnionFind():
    def __init__(self, isConnected):
        n = len(isConnected)
        # self.parent =list(range(n))#存入将被union的数据
        self.count = 0
        self.parent=[0]*n
        for i in range(n):
            self.parent[i] = i
            self.count +=1
        self.rank = [0]*n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.count -= 1


class Solution:
    def findCircleNum1(self, isConnected) -> int:#bfs
        def bfs(i):
            q= collections.deque([i])
            while q:
                i = q.popleft()
                visited.add(i)
                for j in range(n):
                    if isConnected[i][j] == 1 and j not in  visited:
                        q.append(j)

        n = len(isConnected)
        visited = set()
        import collections
        ret = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                ret +=1
        return ret

    def findCircleNum2(self, isConnected) -> int:#dfs
        if not isConnected or not isConnected[0]:return 0
        #O(n*n)
        def dfs(i):
            for j in range(n):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
        n = len(isConnected)
        visited = set()
        ret =0
        for i in range(n):
            if i not in visited:
                dfs(i)
                ret +=1
        return ret

    def findCircleNum3(self, isConnected) -> int:
        if not isConnected or not isConnected[0]:
            return 0
        n = len(isConnected)
        uf = UnionFind(isConnected)
        #时间复杂度O(n^2logn)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        return uf.count


if __name__ == '__main__':
    s = Solution()
    isConnected = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]
    print('1', s.findCircleNum1(isConnected))
    print('2', s.findCircleNum2(isConnected))
    print('3', s.findCircleNum3(isConnected))
    isConnected = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    print('1', s.findCircleNum1(isConnected))
    print('2', s.findCircleNum2(isConnected))
    print('3', s.findCircleNum3(isConnected))
    isConnected = [
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 1],
        [1, 0, 1, 1]
    ]
    print('1', s.findCircleNum1(isConnected))
    print('2', s.findCircleNum2(isConnected))
    print('3', s.findCircleNum3(isConnected))
