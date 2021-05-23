'''
442. 数组中重复的数据
给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。

找到所有出现两次的元素。

你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？
示例：
输入:
[4,3,2,7,8,2,3,1]
输出:
[2,3]
'''
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> List[int]:#标记法
        if not nums:return []
        n = len(nums)
        ret =[]
        #通过数组中的元素推算出新的position，然后取反作为已经被比较过的数
        for i in range(n):
            num = abs(nums[i])
            new_pos = num-1
            if nums[new_pos] < 0:
                ret.append(num)
            else:
                nums[new_pos] = -nums[new_pos]
        return ret


if __name__ == '__main__':
    s = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print('1', s.findDuplicate(nums))
    nums =[4,6,3,2,6,4]
    print('1', s.findDuplicate(nums))
