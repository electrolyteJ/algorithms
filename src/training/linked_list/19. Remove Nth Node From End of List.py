'''
19. 删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗？

示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]
提示：

链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

'''
from common.list import ListNode, create_listnode

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode(-1)
        dummy_head.next = head
        third_place = dummy_head
        first_place,second_place = head,head
        for _ in range(n):
            first_place = first_place.next
       
        while first_place:
            first_place, second_place, third_place = first_place.next, second_place.next, third_place.next
        third_place.next = second_place.next
        return dummy_head.next

if __name__ == '__main__':
    s = Solution()
    head = [1, 2, 3, 4, 5]
    n = 2
    print('1', s.removeNthFromEnd(create_listnode(head), n))
    head = [1]
    n = 1
    print('1', s.removeNthFromEnd(create_listnode(head), n))
    head = [1, 2]
    n = 1
    print('1', s.removeNthFromEnd(create_listnode(head), n))
    head = [1, 2]
    n = 2
    print('1', s.removeNthFromEnd(create_listnode(head), n))
