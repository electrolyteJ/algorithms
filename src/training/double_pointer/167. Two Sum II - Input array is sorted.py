'''
167. 两数之和 II - 输入有序数组
给定一个已按照 升序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。
函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例 1：
输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
示例 2：
输入：numbers = [2,3,4], target = 6
输出：[1,3]
示例 3：
输入：numbers = [-1,0], target = -1
输出：[1,2]
提示：
2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers 按 递增顺序 排列
-1000 <= target <= 1000
仅存在一个有效答案
'''
from typing import List
class Solution:
    def twoSum1(self, numbers: List[int], target: int) -> List[int]:#bisect
        n = len(numbers)
        #时间复杂度O(nlogn)
        for i in range(n):
            l,r=i+1,n-1
            while l <=r:
                mid = (l+r)>>1
                if numbers[mid] == target-numbers[i]:
                    return [i+1,mid+1]
                elif numbers[mid] > target-numbers[i]:
                    r = mid-1
                else:
                    l = mid+1
        return [-1,-1]

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:#双指针
        n = len(numbers)
        l,r=0,n-1
        #时间复杂度复杂度O(n)
        while l < r:
            sum_ret = numbers[l]+numbers[r]
            if sum_ret ==target:
                return [l+1,r+1]
            elif sum_ret > target:
                r -=1
            else:
                l+=1
        return [-1,-1]
            
if __name__ =='__main__':
    s = Solution()
    numbers = [2, 7, 11, 15]; target = 9
    print('1',s.twoSum1(numbers, target))
    print('2',s.twoSum2(numbers, target))
    numbers = [2, 3, 4]; target = 6
    print('1',s.twoSum1(numbers, target))
    print('2',s.twoSum2(numbers, target))
    numbers = [-1, 0]; target = -1
    print('1',s.twoSum1(numbers, target))
    print('2',s.twoSum2(numbers, target))
