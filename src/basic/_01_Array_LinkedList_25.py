'''
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
'''

from mock.ListNode import ListNode


class Solution:  # linked list :1->2->3->4->5->None
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):
        cur_node = head
        ret_node = tail
        while cur_node != tail:

            tmp = cur_node.next
            cur_node.next = ret_node
            ret_node = cur_node
            cur_node = tmp

        return ret_node, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy_head = ListNode(0)
        dummy_head.next = head
        cur = dummy_head

        while head:
            dummy_tail = cur
            for i in range(k):
                dummy_tail = dummy_tail.next
                if not dummy_tail:
                    return dummy_head.next
            tail = dummy_tail.next
            # print('before', head, dummy_tail)
            head, dummy_tail = self.reverse(head, tail)
            print('after', head, dummy_tail)
            # 把子链表重新接回原链表
            cur.next = head
            dummy_tail.next = tail
            cur = dummy_tail
            head = dummy_tail.next
        return dummy_head.next


def main():
    datas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    listnode = ListNode.create(datas)
    print('raw datas: {}'.format(listnode))
    s = Solution()
    print('k =2 {}'.format(s.reverseKGroup(listnode, 4)))
    listnode2 = ListNode.create(datas)
    # print('k = 3 {}'.format(s.reverseKGroup(listnode2, 3)))


if __name__ == '__main__':
    main()
