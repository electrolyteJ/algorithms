'''
189. 旋转数组
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
进阶：

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
示例 1:
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
提示：

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

'''
class Solution:
    def rotate1(self, nums, k: int) -> None:
        n = len(nums)
        #时间复杂度O(n) 空间复杂度O(n)
        rotate = [0]*n
        for i in range(n):
            rotate[(i+k) % n] = nums[i]
        for i in range(n):
            nums[i] = rotate[i]

    def rotate2(self, nums, k: int) -> None:
        def gcd( x,  y):
            return gcd(y, x % y) if y > 0 else x
        n = len(nums)
        k =k %n
        count = gcd(k,n)
        #时间复杂度O(n) 空间复杂度O(1)
        for i in range(count):
            cur = i
            pre = nums[i]
            while True:
                next_i = (cur + k) % n

                nums[next_i], pre = pre, nums[next_i]
                cur =next_i
                if i == cur:
                    break

    def rotate3(self, nums, k: int) -> None:
        #时间复杂度O(n) 空间复杂度O(1)
        def reverse(nums,start,end):
            while start < end:
                nums[start],nums[end] = nums[end],nums[start]
                start +=1
                end -=1
        k %=len(nums)
        reverse(nums,0,len(nums)-1)
        reverse(nums,0,k-1)
        reverse(nums,k,len(nums)-1)

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print('1', s.rotate1(nums, k),nums)
    nums = [1, 2, 3, 4, 5, 6, 7]
    print('2', s.rotate2(nums, k), nums)
    nums = [1, 2, 3, 4, 5, 6, 7]
    print('3', s.rotate3(nums, k), nums)
    nums = [1, 2]
    k = 3
    print('1', s.rotate1(nums, k), nums)  # [2,1]
    nums = [1, 2]
    print('2', s.rotate2(nums, k), nums)
    nums = [1, 2]
    print('3', s.rotate3(nums, k), nums)
