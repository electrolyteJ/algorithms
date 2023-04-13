"""
25. K 个一组翻转链表
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例：

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明：

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
"""

from common.list import ListNode, create_listnode


class Solution:  # linked list :1->2->3->4->5->None
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 翻转一个子链表，并且返回新的头与尾
        def reverse(head, tail):
            if not head:return
            cur = head
            new_head = tail
            while cur != tail:
                cur.next, cur, new_head = new_head, cur.next, cur
            return new_head, head

        dummy_head = ListNode(-1)
        dummy_head.next = head
        hair = dummy_head
        while head:
            foot = hair
            for _ in range(k):
                foot = foot.next
                if not foot:
                    return dummy_head.next
            tail = foot.next
            head, foot = reverse(hair.next, tail)
            hair.next, hair = head, foot
        return dummy_head.next


def main():
    datas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    listnode = create_listnode(datas)
    print('raw datas: {}'.format(listnode))
    s = Solution()
    print('k =2 {}'.format(s.reverseKGroup(listnode, 2)))
    listnode2 = create_listnode(datas)
    print('k = 3 {}'.format(s.reverseKGroup(listnode2, 3)))


if __name__ == '__main__':
    main()
