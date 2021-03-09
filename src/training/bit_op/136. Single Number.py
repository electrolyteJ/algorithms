'''
136. 只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4
'''

import functools
class Solution:
    def singleNumber(self, nums) -> int:
        '''
        异或运算有以下三个性质。
        1.任何数和 00 做异或运算，结果仍然是原来的数，即 a \oplus 0=aa⊕0=a。
        2.任何数和其自身做异或运算，结果是 00，即 a \oplus a=0a⊕a=0。
        3.异或运算满足交换律和结合律，即 a \oplus b \oplus a=b \oplus a \oplus a=b \oplus (a \oplus a)=b \oplus0=ba⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)=b⊕0=b。

        '''
        return functools.reduce(lambda x, y: x ^ y, nums)
if __name__ =='__main__':
    s = Solution()
    nums = [2, 2, 1]
    print('1',s.singleNumber(nums))
    nums = [4, 1, 2, 1, 2]
    print('1',s.singleNumber(nums))
