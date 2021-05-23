'''
287. 寻找重复数
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。

示例 1：
输入：nums = [1,3,4,2,2]
输出：2
示例 2：
输入：nums = [3,1,3,4,2]
输出：3
示例 3：
输入：nums = [1,1]
输出：1
示例 4：
输入：nums = [1,1,2]
输出：1
提示：
2 <= n <= 3 * 104
nums.length == n + 1
1 <= nums[i] <= n
nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次
进阶：
如何证明 nums 中至少存在一个重复的数字?
你可以在不修改数组 nums 的情况下解决这个问题吗？
你可以只用常量级 O(1) 的额外空间解决这个问题吗？
你可以设计一个时间复杂度小于 O(n2) 的解决方案吗？
'''
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:  # 标记法
        #时间复杂度O(n)
        n = len(nums)
        for i in range(n):
            num = abs(nums[i])
            if nums[num-1]<0:
                return num
            else:
                nums[num-1] =- nums[num-1]
        return -1
    def findDuplicate1(self, nums: List[int]) -> int:#bisect
        #时间复杂度O(nlogn)
        n = len(nums)
        l,r= 1,n
        # 1 2 3 4 5 6 7 ... 10 ... n
        while l < r:
            mid = (l+r)>>1
            cnt=0
            for i in range(n):
                if nums[i] <= mid:
                    cnt +=1
            if cnt <= mid:
                l = mid+1
            else:
                r =mid
        return l

                
    def findDuplicate2(self, nums: List[int]) -> int:
        pass

    #对数组建成图，每个位置i的连一条i --> nums[i]的边，检查图是否有环
    def findDuplicate3(self, nums: List[int]) -> int:  # 快慢指针,Floyd 判圈算法
        slow, fast = nums[0], nums[nums[0]]
        #时间复杂度O(n)
        while slow !=fast:
           slow, fast = nums[slow], nums[nums[fast]]
        slow2 =0
        while slow2 != slow:
            slow2, slow = nums[slow2], nums[slow]
        return slow

if __name__ =='__main__':
    s = Solution()
    nums = [1, 3, 4, 2, 2]
    print('1',s.findDuplicate1(nums))
    print('2',s.findDuplicate2(nums))
    print('3',s.findDuplicate3(nums))
    nums = [3, 1, 3, 4, 2]
    print('1',s.findDuplicate1(nums))
    print('2', s.findDuplicate2(nums))
    print('3', s.findDuplicate3(nums))
    nums = [1, 1]
    print('1',s.findDuplicate1(nums))
    print('2', s.findDuplicate2(nums))
    print('3', s.findDuplicate3(nums))
    nums = [1, 1, 2]
    print('1',s.findDuplicate1(nums))
    print('2', s.findDuplicate2(nums))
    print('3', s.findDuplicate3(nums))
