'''
剑指 Offer 56 - II. 数组中数字出现的次数 II
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
示例 1：

输入：nums = [3,4,3,3]
输出：4
示例 2：

输入：nums = [9,1,7,9,7,9,7]
输出：1
 

限制：

1 <= nums.length <= 10000
1 <= nums[i] < 2^31
'''


class Solution:
    def singleNumber(self, nums) -> int:
        #时间复杂度O(n) 空间复杂度O(n)
        import collections
        d = collections.defaultdict(int)
        for num in nums:
            d[num] +=1
        for k,v in d.items():
            if v!=3:
                return k
        return 0
    def singleNumber2(self, nums) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones

if __name__ =='__main__':
    s =Solution()
    nums = [3, 4, 3, 3]
    print('1', s.singleNumber(nums))
    nums = [9, 1, 7, 9, 7, 9, 7]
    print('1', s.singleNumber(nums))
