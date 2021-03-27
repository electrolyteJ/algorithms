'''
77. 组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(pos,k,n):
            #剪枝
            if (len(visited) + n-pos+1)<k:
                return
            if len(visited) ==k:
                ret.append(visited[:])
                return
            if pos == n+1:
                return 
            visited.append(pos)
            backtrack(pos+1,k,n)
            visited.pop()            
            backtrack(pos+1,k,n)
        ret = []
        visited=[]
        backtrack(1, k, n)
        return ret
if __name__ =='__main__':
    s = Solution()
    n = 4;k = 2
    print('1',s.combine(n,k))
