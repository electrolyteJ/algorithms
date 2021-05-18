'''
200. 岛屿数量
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。
示例 1：
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：
输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
提示：
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'
'''
class UnionFind():
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1]*(m*n)
        self.rank = [0]*(m*n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[i*n+j] = i*n+j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        #todo 路径压缩,O(lgn)
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        #用rank实现优化合并，矮树并入高数,O(lgn)
        if rootx != rooty: 
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1

class Solution:
    # 类变量
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def numIslands1(self, grid) -> int:  # bfs
        if not grid or not grid[0]:
            return 0
        import collections

        def floadfill_bfs(x, y):
            if not (
               0 <= x < len(grid)
               and 0 <= y < len(grid[0])
               and grid[x][y] == '1'
               and ((x, y) not in visited)
            ):
                return 0
            visited.add((x, y))
            q = collections.deque([(x, y)])
            while q:
                cur_x, cur_y = q.popleft()
                for i in range(4):
                    new_x, new_y = cur_x+self.dx[i], cur_y+self.dy[i]
                    tp = (new_x, new_y)
                    if (0 <= new_x < len(grid)
                            and 0 <= new_y < len(grid[0])
                            and grid[new_x][new_y] == '1'
                            and (tp not in visited)
                    ):
                        visited.add(tp)
                        q.append(tp)
            return 1

        visited = set()
        return sum([floadfill_bfs(i, j) for i in range(len(grid)) for j in range(len(grid[0]))])

    def numIslands2(self, grid) -> int:  # dfs
        if not grid or not grid[0]:
            return 0
        #时间复杂度O(m*n) 空间复杂度O(m*n)
        def floadfill_dfs(x, y):
            if not (
                0 <= x < len(grid) 
                and 0 <= y < len(grid[0]) 
                and grid[x][y] == '1' 
                and ((x, y) not in visited)
            ):
                return 0
            visited.add((x, y))
            for k in range(4):
                floadfill_dfs(x+self.dx[k], y+self.dy[k])
            return 1

        visited = set()
        return sum([floadfill_dfs(i, j) for i in range(len(grid)) for j in range(len(grid[0]))])

    def numIslands3(self, grid) -> int:  # disjoinset
       
        if not grid or not grid[0]:return 0
        uf = UnionFind(grid)
        directions = [
            [0, 1],
            [0, -1],
            [-1, 0],
            [1, 0],
        ]
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                for d in directions:
                    nr, nc = i+d[0], j+d[1]
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                        uf.union(i*n+j, nr*n+nc)
        return uf.count


if __name__ == '__main__':
    s = Solution() #0,1 
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print('1', s.numIslands1(grid))  # 1
    print('2', s.numIslands2(grid))  # 1
    print('3', s.numIslands3(grid))  # 1
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print('1', s.numIslands1(grid))  # 3
    print('2', s.numIslands2(grid))  # 1
    print('3', s.numIslands3(grid))  # 1
    # print(Solution.a)
