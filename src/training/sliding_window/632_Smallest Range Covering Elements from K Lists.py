'''
632. 最小区间
你有 k 个 非递减排列 的整数列表。找到一个 最小 区间，使得 k 个列表中的每个列表至少有一个数包含在其中。

我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。

示例 1：

输入：nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
输出：[20,24]
解释：
列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
示例 2：

输入：nums = [[1,2,3],[1,2,3],[1,2,3]]
输出：[1,1]
示例 3：

输入：nums = [[10,10],[11,11]]
输出：[10,11]
示例 4：

输入：nums = [[10],[11]]
输出：[10,11]
示例 5：

输入：nums = [[1],[2],[3],[4],[5],[6],[7]]
输出：[1,7]

提示：

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 10^5
nums[i] 按非递减顺序排列
'''
class Solution:
    def smallestRange1(self, nums):  # 小顶堆
        import heapq
        pq = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(pq)
        #时间复杂度O(nklogk) 空间复杂度取决于堆大小 O(k)
        ans = -1e9, 1e9
        right = max(row[0] for row in nums)
        while pq:
            left, r, c = heapq.heappop(pq)
            if right - left < ans[1] - ans[0]:
                ans = left, right
            if c + 1 == len(nums[r]):
                return ans
            right = max(right, nums[r][c+1])
            heapq.heappush(pq, (nums[r][c+1], r, c+1))

    def smallestRange2(self, nums):  #滑动窗口
        if not nums: return None
        n = len(nums)
        import collections
        indices = collections.defaultdict(list)
        xMin, xMax = 10**9, -10**9
        for i, vec in enumerate(nums):
            for x in vec:
                indices[x].append(i)
            xMin = min(xMin, *vec)
            xMax = max(xMax, *vec)

        freq = [0] * n
        inside = 0
        left, right = xMin, xMin - 1
        bestLeft, bestRight = xMin, xMax

        while right < xMax:
            right += 1
            if right in indices:
                for x in indices[right]:
                    freq[x] += 1
                    if freq[x] == 1:
                        inside += 1
                while inside == n:
                    if right - left < bestRight - bestLeft:
                        bestLeft, bestRight = left, right
                    if left in indices:
                        for x in indices[left]:
                            freq[x] -= 1
                            if freq[x] == 0:
                                inside -= 1
                    left += 1

        return [bestLeft, bestRight]

if __name__ == '__main__':
    s = Solution()
    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    print('1', s.smallestRange1(nums))
    print('2', s.smallestRange2(nums))
    nums = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    print('1', s.smallestRange1(nums))
    print('2', s.smallestRange2(nums))
    nums = [[10, 10], [11, 11]]
    print('1', s.smallestRange1(nums))
    print('2', s.smallestRange2(nums))
    nums = [[10], [11]]
    print('1', s.smallestRange1(nums))
    print('2', s.smallestRange2(nums))
    nums = [[1], [2], [3], [4], [5], [6], [7]]
    print('1', s.smallestRange1(nums))
    print('2', s.smallestRange2(nums))
