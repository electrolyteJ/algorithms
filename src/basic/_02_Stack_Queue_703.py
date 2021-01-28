'''
703. 数据流中的第 K 大元素
设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。

请实现 KthLargest 类：

KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。


示例：

输入：
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
输出：
[null, 4, 5, 5, 8, 8]

解释：
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8


提示：
1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
最多调用 add 方法 104 次
题目数据保证，在查找第 k 大元素时，数组中至少有 k 个元素
'''
from queue import PriorityQueue
import heapq


class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif self.nums[0] < val:
            heapq.heappushpop(self.nums, val)
        return self.nums[0]


class KthLargest2:

    def __init__(self, k: int, nums):
        self.k = k
        self.q = PriorityQueue(k)
        for e in nums:
            self.add(e)

    def add(self, val: int) -> int:
        if self.q.qsize() < self.k:
            self.q.put(val)
        elif self.q.queue[0] < val:
            self.q.get()
            self.q.put(val)
        return self.q.queue[0]


def main():

    l = [4, 2, 5, 1, 3]
    ks = KthLargest(4, l)
    # print(ks.nums)
    # print(ks.add(4))
    # print(ks.nums)
    # print(ks.add(2))
    # print(ks.nums)
    # print(ks.add(5))
    # print(ks.nums)
    # print(ks.add(1))
    # print(ks.nums)
    # print(ks.add(3))
    # print(ks.nums)

    ks = KthLargest2(4, [4, 2, 5, 1, 3])
    print(ks.q.queue)
    print(ks.add(4))
    print(ks.q.queue)
    print(ks.add(2))
    print(ks.q.queue)
    print(ks.add(5))
    print(ks.q.queue)
    print(ks.add(1))
    print(ks.q.queue)
    print(ks.add(3))
    print(ks.q.queue)


if __name__ == '__main__':
    main()
