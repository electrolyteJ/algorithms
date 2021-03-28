'''
23. 合并K个升序链表
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。
示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]

提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4
'''
from typing import List
from src.common.list import ListNode, create_listnode


class Solution:
    def merge(self, l1, l2):
        if not l1 or not l2:
            return l1 if l1 else l2
        dummy_head = ListNode(-1)
        l = dummy_head
        while l1 and l2:
            if l1.value < l2.value:
                l.next, l, l1 = l1, l1, l1.next
            else:
                l.next = l2
                l = l2
                l2 = l2.next
        l.next = l1 if l1 else l2
        return dummy_head.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        ans = lists[0]
        # 时间复杂度O(k^2 * n)
        for i in range(1, len(lists)):
            ans = self.merge(ans, lists[i])
        return ans

    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        # 时间复杂度O(kn * logk) 空间复杂度O(logk)
        def merge_list(l, r):
            if l == r:
                return lists[l]
            if l > r:
                return None
            mid = l+(r-l)//2
            return self.merge(merge_list(l, mid), merge_list(mid+1, r))
        return merge_list(0, len(lists)-1)

    def mergeKLists3(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        import heapq,queue
        #时间复杂度O(kn * logk) 空间复杂度O(k)
        q= []
        for l in lists:
            heapq.heappush(q,(l.value,l))
        dummy_head = ListNode(-1)
        tail= dummy_head
        while q:
            v,node = heapq.heappop(q)
            tail.next,tail = node,node
            if node.next:
                heapq.heappush(q,(node.next.value,node.next))
        return dummy_head.next


if __name__ == '__main__':
    s = Solution()
    lists = []
    for l in [[1, 4, 5], [1, 3, 4], [2, 6]]:
        lists.append(create_listnode(l))
    print(lists)
    print('1', s.mergeKLists(lists))
    lists = []
    for l in [[1, 4, 5], [1, 3, 4], [2, 6]]:
        lists.append(create_listnode(l))
    print('2', s.mergeKLists2(lists))
    lists = []
    for l in [[1, 4, 5], [1, 3, 4], [2, 6]]:
        lists.append(create_listnode(l))
    print('3', s.mergeKLists3(lists))
