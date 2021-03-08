'''
82. 删除排序链表中的重复元素 II
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3
'''
from src.common.list import create_listnode, ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(-1)
        dummy_head.next = head
        pre, cur = dummy_head, head
        #时间复杂度O(n) 空间复杂度O(1)
        while cur and cur.next:

            if cur.value == cur.next.value:
                while cur.next and cur.value == cur.next.value:
                    cur.next = cur.next.next
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next

        return dummy_head.next


if __name__ == '__main__':
    s = Solution()
    head = create_listnode([1, 2, 3, 3, 3, 4, 4, 5])
    print('1', s.deleteDuplicates(head))
    head = create_listnode([1, 1, 1, 2, 3])
    print('1', s.deleteDuplicates(head))
