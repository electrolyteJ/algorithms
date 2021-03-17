'''
315. 计算右侧小于当前元素的个数
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。
示例：

输入：nums = [5,2,6,1]
输出：[2,1,1,0] 
解释：
5 的右侧有 2 个更小的元素 (2 和 1)
2 的右侧仅有 1 个更小的元素 (1)
6 的右侧有 1 个更小的元素 (1)
1 的右侧有 0 个更小的元素

提示：

0 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

'''
class Solution:
    def countSmaller(self, nums):
        #时间复杂度O(nlogn)  空间复杂度O(n)
        def merge_sort(left,right):
            if left>=right:
                return
            mid= left+(right-left)//2
            merge_sort(left,mid)
            merge_sort(mid+1,right)

            i,j=left,mid+1
            tmp[left:right+1] = indexes[left:right+1]
            for k in range(left,right+1):
                if i == mid+1:
                    indexes[k] = tmp[j]
                    j+=1
                elif j == right+1:
                    indexes[k] = tmp[i]
                    i +=1
                    res[indexes[k]] += right - mid
                elif nums[tmp[i]] <= nums[tmp[j]]:
                    indexes[k] = tmp[i]
                    i +=1
                    res[indexes[k]] += j -1- mid
                else:#左边的数据大于右边
                    indexes[k] = tmp[j]
                    j+=1

        n = len(nums)
        tmp = [0]*n
        indexes = [i for i in range(n)]
        res = [0]*n
        merge_sort(0,n-1)
        return res

if __name__ == '__main__':
    s = Solution()
    nums = [5, 2, 6, 1]
    print('1',s.countSmaller(nums))
    nums = [-1, -1]
    print('1',s.countSmaller(nums))
    nums = [0, 2, 1]
    print('1',s.countSmaller(nums))
