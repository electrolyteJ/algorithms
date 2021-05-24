'''
45. 跳跃游戏 II
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
假设你总是可以到达数组的最后一个位置。
示例 1:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
示例 2:

输入: [2,3,0,1,4]
输出: 2
提示:
1 <= nums.length <= 1000
0 <= nums[i] <= 105
'''
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        steps=0
        rightmost =0
        end = 0
        for i in range(n-1):
            rightmost = max(rightmost,i+nums[i])
            if i == end:
                end = rightmost
                steps +=1
        return steps
if __name__ =='__main__':
    s = Solution()
    nums = [2, 3, 1, 1, 4]
    print('1',s.jump(nums))
    nums = [2, 3, 0, 1, 4]
    print('1',s.jump(nums))
