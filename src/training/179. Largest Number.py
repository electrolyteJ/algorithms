'''
179. 最大数
给定一组非负整数 nums，重新排列它们每个数字的顺序（每个数字不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

示例 1：

输入：nums = [10,2]
输出："210"
示例 2：

输入：nums = [3,30,34,5,9]
输出："9534330"
示例 3：

输入：nums = [1]
输出："1"
示例 4：

输入：nums = [10]
输出："10"
 

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 109
'''


class Solution:
    def largestNumber(self, nums) -> str:
        def quick_sort(strs,l,r):
            if l >= r:
                return
            i,j=l,r
            pivot = strs[l]
            while i<j:
                #x+y > y+x   x>y
                while i <j and strs[j]+pivot <= pivot+strs[j]:
                    j-=1
                while i<j and strs[i]+pivot >=pivot+strs[i]:
                    i+=1
                strs[i],strs[j]=strs[j],strs[i]
            strs[i],strs[l]=strs[l],strs[i]
            quick_sort(strs,l,i-1)
            quick_sort(strs,i+1,r)
        strs=[str(num) for num in nums]
        quick_sort(strs,0,len(strs)-1)
        return '0' if strs[0] == '0' else ''.join(strs)
if __name__ =='__main__':
    s = Solution()
    nums = [10, 2]
    print('1',s.largestNumber(nums))
    nums = [3, 30, 34, 5, 9]
    print('1',s.largestNumber(nums))
    nums = [1]
    print('1',s.largestNumber(nums))
    nums = [10]
    print('1',s.largestNumber(nums))
