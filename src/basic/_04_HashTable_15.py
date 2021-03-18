'''
15. 三数之和
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]
 

提示：

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
通过次数407,802提交次数1,329,201
'''


class Solution:

    def threeSum(self, nums):#sort and find
        if not nums or len(nums) < 3:
            return []
        ret = []
        nums.sort()
        size = len(nums)
        #时间复杂度为O(n*n)
        for i, e1 in enumerate(nums[:-2]):
            if i > 0 and e1 == nums[i-1]:
                continue
            l,r = i+1,size-1
            while l<r:
                s = e1+nums[l]+nums[r]
                if s <0:
                    l +=1
                elif s>0:
                    r-=1
                else:
                    ret.append([e1,nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r] == nums[r-1]:
                        r -=1
                    l+=1;r-=1
                
        return ret
    def threeSum1(self, nums):  # sort and find
        if not nums or len(nums) < 3:
            return []
        ret = []
        s_nums = sorted(nums)
        size = len(s_nums)
        for first in range(0, size):
            e1 = s_nums[first]
            if first > 0 and e1 == s_nums[first-1]:
                continue
            third = size-1
            for sec in range(first+1, size):
                e2 = s_nums[sec]
                if sec > first+1 and e2 == s_nums[sec-1]:
                    continue
                while sec < third and e2+s_nums[third] > -e1:
                    third -= 1
                if sec == third:
                    break
                if e2+s_nums[third] == -e1:
                    ret.append([e1, e2, s_nums[third]])
        return ret

    def threeSum2(self, nums): #set
        if not nums or len(nums) < 3:
            return []
        nums.sort()
        ret =set()
        #时间复杂度为O(n*n) 空间复杂度O(n)
        for i,e1 in enumerate(nums[:-2]):
            if i>=1 and e1==nums[i-1]:
                continue
            # d=dict()
            s = set()
            for e2 in nums[i+1:]:
                y = -(e1 + e2)
                # if e2 not in d:
                if e2 not in s:
                    # d[y]=1
                    s.add(y)
                else:
                    ret.add((e1,y,e2))
        return list(ret)


if __name__ == '__main__':
    s = Solution()
    nums = nums = [-1, 0, 1, 2, -1, -4]
    print(s.threeSum2(nums))
    print(s.threeSum(nums))