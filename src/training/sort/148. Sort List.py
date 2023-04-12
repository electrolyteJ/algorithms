'''
148. 排序链表
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
示例 1：
输入：head = [4,2,1,3]
输出：[1,2,3,4]
示例 2：

输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
示例 3：

输入：head = []
输出：[]

提示：

链表中节点的数目在范围 [0, 5 * 104] 内
-105 <= Node.val <= 105
'''
from common.list import ListNode, create_listnode
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 时间复杂度O(n logn) 空间复杂度O(n logn)
        def merge(l1, l2):
            dummy_head = ListNode(-1)
            l = dummy_head
            while l1 and l2:
                if l1.value <= l2.value:
                    l.next = l1
                    l1 = l1.next
                else:
                    l.next = l2
                    l2 = l2.next
                l = l.next
            l.next = l2 if l2 else l1
            return dummy_head.next

        def merge_sort(head, tail):
            if not head:
                return head
            if head .next == tail:
                head.next = None
                return head
            #1  5   3   4  0->tail   4  2   1   3->tail
            #          mid                  mid
            slow = fast = head#找中间点
            while fast != tail:
                slow, fast = slow.next, fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(merge_sort(head, mid), merge_sort(mid, tail))

        return merge_sort(head, None)

    def sortList2(self, head: ListNode) -> ListNode:
        if not head:
            return
        # 时间复杂度O(n logn) 空间复杂度O(1)
        def merge(l1, l2):
            dummy_head = ListNode(-1)
            l = dummy_head
            while l1 and l2:
                if l1.value <= l2.value:
                    l.next = l1
                    l1 = l1.next
                else:
                    l.next = l2
                    l2 = l2.next
                l = l.next
            l.next = l2 if l2 else l1
            return dummy_head.next
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummyHead = ListNode(-1)
        dummyHead.next =head
        subLength = 1
        while subLength < length:
            prev, curr = dummyHead, dummyHead.next
            while curr:
                head1 = curr
                for i in range(1, subLength):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                head2 = curr.next
                curr.next = None
                curr = head2
                for i in range(1, subLength):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break

                succ = None
                if curr:
                    succ = curr.next
                    curr.next = None

                merged = merge(head1, head2)
                prev.next = merged
                while prev.next:
                    prev = prev.next
                curr = succ
            subLength <<= 1

        return dummyHead.next


if __name__ == '__main__':
    s = Solution()
    head = create_listnode([4, 2, 1, 3])
    print(head)
    print('1', s.sortList(head))
    head = create_listnode([4, 2, 1, 3])
    print('2', s.sortList2(head))
    head = create_listnode([-1, 5, 3, 4, 0])
    print(head)
    print('1', s.sortList(head))
    head = create_listnode([-1, 5, 3, 4, 0])
    print('2', s.sortList2(head))
