'''
42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9

提示：

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105
'''


class Solution:
    def trap(self, height) -> int:  # dp
        if not height:
            return 0
        # 时间复杂度O(n) 空间复杂度O(n)
        n = len(height)
        leftMax = [height[0]] + [0]*(n-1)
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i])
        rightMax = [0]*(n-1)+[height[-1]]
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])
        ans = sum([min(leftMax[i], rightMax[i])-height[i] for i in range(n)])
        return ans

    def trap2(self, height) -> int:  # 双指针
        if not height:
            return 0
        n = len(height)
        # 时间复杂度O(n) 空间复杂度O(1)
        left, right = 0, n-1
        leftMax, rightMax = 0, 0
        ret = 0
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if leftMax <= rightMax:
                ret += leftMax-height[left]
                left += 1
            else:
                ret += rightMax-height[right]
                right -= 1
        return ret

    def trap3(self, height) -> int:  # stack
        if not height:
            return 0
        # 时间复杂度O(n) 空间复杂度O(n)
        stack = []
        n = len(height)
        ret = 0
        for i in range(n):
            while stack and height[stack[-1]] < height[i]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                curWidth = i - left - 1
                curHeight = min(height[left], height[i]) - height[top]
                ret += curWidth * curHeight
            stack.append(i)
        return ret


if __name__ == '__main__':
    s = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print('1', s.trap(height))
    print('2', s.trap2(height))
    print('3', s.trap3(height))
    height = [4, 2, 0, 3, 2, 5]
    print('1', s.trap(height))
    print('2', s.trap2(height))
    print('3', s.trap3(height))
