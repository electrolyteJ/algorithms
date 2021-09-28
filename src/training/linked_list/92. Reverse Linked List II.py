'''
92. 反转链表 II
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
'''

from src.common.list import create_listnode,ListNode
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        #遍历了两次
        if not head:
            return
        dummy_head = ListNode(-1)
        pre = dummy_head
        pre.next = head
        start = head
        for _ in range(left-1):
            start = start.next
            pre = pre.next

        tail = head
        for _ in range(right):
            tail = tail.next

        def reverse(s, tail):
            if not s:
                return None
            ret = tail
            cur = s
            while cur and cur != tail:
                cur.next, cur, ret = ret, cur.next, cur
            return ret
        r = reverse(start, tail)
        pre.next = r
        return dummy_head.next
    def reverseBetween2(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy_head = ListNode(-1)
        dummy_head.next = head
        pre = dummy_head
        for _ in range(left-1):
            pre = pre.next
        cur = pre.next
        for _ in range(right - left):
            next = cur.next
            cur.next, next.next, pre.next = next.next, pre.next, next
        return dummy_head.next

if __name__ =='__main__':
    s = Solution()
    head = create_listnode([1 ,2,3 ,4 ,5])
    left,right=2,4
    print('1',s.reverseBetween(head,left,right))
    head = create_listnode([1 ,2,3 ,4 ,5])
    print('2',s.reverseBetween2(head,left,right))
