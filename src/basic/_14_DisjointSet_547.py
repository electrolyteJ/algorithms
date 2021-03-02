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
        m, n = len(isConnected), len(isConnected[0])
        self.counter = 0
        self.parent = [-1]*m*n
        self.rank = [0]*m*n
        for i in range(m):
            for j in range(n):
                if isConnected[i][j] == 1:
                    self.parent[i*n+j] = i*n+j
                    self.counter += 1

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
                self.rank[rootx] += 1
            self.counter -= 1


class Solution:
    def findCircleNum1(self, isConnected) -> int:#bfs
        provinces = len(isConnected)
        visited = set()
        circles = 0
        import collections
        for i in range(provinces):
            if i not in visited:
                Q = collections.deque([i])
                while Q:
                    j = Q.popleft()
                    visited.add(j)
                    for k in range(provinces):
                        if isConnected[j][k] == 1 and k not in visited:
                            Q.append(k)
                circles += 1
        
        return circles

    def findCircleNum2(self, isConnected) -> int:#dfs
        if not isConnected or not isConnected[0]:
            return 0
        #O(n^2)
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
        m, n = len(isConnected), len(isConnected[0])
        uf = UnionFind(isConnected)
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(m):
            for j in range(n):
                if isConnected[i][j] == 0:
                    continue
                for k in range(4):
                    x, y = i+dx[k], j+dy[k]
                    if 0 <= x < m and 0 <= y < n and isConnected[x][y] == 1:
                        uf.union(i*n+j, x*n+y)

        return uf.counter


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
