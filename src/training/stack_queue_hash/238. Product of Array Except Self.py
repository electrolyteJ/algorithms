'''
238. 除自身以外数组的乘积
给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
 

提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。

说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
'''


class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ret=[]
        #时间复杂度(n*n)
        for i in range(n):
            multipy_ret=1
            for j in range(n):
                if i !=j:
                    multipy_ret *= nums[j]
            ret.append(multipy_ret)
        return ret
    def productExceptSelf2(self, nums):
        ret = []
        n = len(nums)
        l = [1]*n
        for i in range(1,n):
            l[i] = l[i-1]*nums[i-1]
        r=[1]*n
        for i in range(n-2,-1,-1):
            r[i] =r[i+1]*nums[i+1]
        ret=[]
        for i in range(n):
            ret.append(l[i]*r[i])
        return ret

    def productExceptSelf3(self, nums):
        n = len(nums)
        ret = [1]*n
        for i  in range(1,n):
            ret[i] = ret[i-1]*nums[i-1]
        r=1
        for i in range(n-2,-1,-1):
            r *=nums[i+1]
            ret[i]=ret[i] * r
        return ret

if __name__ =='__main__':
    s = Solution()
    nums = [1, 2, 3, 4]
    print('1',s.productExceptSelf(nums))
    print('1', s.productExceptSelf2(nums))
    print('1', s.productExceptSelf3(nums))
