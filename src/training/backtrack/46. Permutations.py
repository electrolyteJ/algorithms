'''
46. 全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''


class Solution:
    def permute(self, nums):
        #时间复杂度O(n*n!)
        def backtrack():
            if len(visited) == len(nums):
                ret.append(list(visited))
                return
            for i in range(len(nums)):
                num = nums[i]
                if num not in visited:
                    visited.append(num)
                    backtrack()
                    visited.pop()

        ret=[]
        visited=[]
        backtrack()
        return ret
    def permute2(self, nums):
        #时间复杂度O(n*n!)
        def backtrack(pos):
            if pos == len(nums):
                ret.append(nums[:])
            for i in range(pos,len(nums)):
                nums[i],nums[pos] = nums[pos],nums[i]
                backtrack(pos+1)
                nums[i],nums[pos] = nums[pos],nums[i]
        ret=[]
        backtrack(0)
        return ret

if __name__ == '__main__':
    s = Solution()
    ns = [1, 2, 3]
    print('1',s.permute(ns))
    print('2', s.permute2(ns))
