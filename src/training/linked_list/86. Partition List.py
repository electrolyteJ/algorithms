'''
86. 分隔链表
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。

示例 1：

输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]
示例 2：

输入：head = [2,1], x = 2
输出：[1,2]

提示：

链表中节点的数目在范围 [0, 200] 内
-100 <= Node.val <= 100
-200 <= x <= 200
'''

from common.list import create_listnode,ListNode
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:return
        s_dummy_head,l_dummy_head = ListNode(-1),ListNode(-1)
        small_foot, large_foot = s_dummy_head, l_dummy_head
        while head:
            if head.value < x:
                small_foot.next = head
                small_foot = small_foot.next
            else:
                large_foot.next = head
                large_foot = large_foot.next
            head = head.next

        large_foot.next = None
        small_foot.next = l_dummy_head.next
        return s_dummy_head.next

if __name__ == '__main__':
    s = Solution()
    head = create_listnode([1, 4, 3, 2, 5, 2])
    x = 3
    print(head)
    print('1', s.partition(head, x))
    head = create_listnode([2, 1])
    x = 2
    print(head)
    print('1', s.partition(head, x))
