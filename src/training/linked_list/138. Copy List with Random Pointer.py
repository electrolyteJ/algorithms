'''
138. 复制带随机指针的链表
给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。

例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。

返回复制链表的头节点。

用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
你的代码 只 接受原链表的头节点 head 作为传入参数。

示例 1：

输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
示例 2：

输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
示例 3：

输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
示例 4：

输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
 
提示：

0 <= n <= 1000
-10000 <= Node.val <= 10000
Node.random 为空（null）或指向链表中的节点。
'''
from common.list import create_listnode,ListNode
class Solution:
    def copyRandomList(self, head):
        if not head:
            return
        visited = {}
        #时间复杂度O(n) 空间复杂度O(n)
        def recur(node):
            if not node:
                return
            if node in visited:
                return visited[node]
            new_node = ListNode(node.value,True)
            visited[node] = new_node
            new_node.next = recur(node.next)
            new_node.random = recur(node.random)
            return new_node
        return recur(head)

    def copyRandomList2(self, head):
        if not head:return 
        #时间复杂度O(n) 空间复杂度O(n)
        def clone_node(node):
            if not node:return
            if node not in visited:
                visited[node] = ListNode(node.value, True)
            return visited[node]

        visited ={}
        old_head,new_head = head,ListNode(head.value,True)
        visited[old_head] = new_head
        while old_head:

            new_head.next = clone_node(old_head.next)
            new_head.random = clone_node(old_head.random)
            
            new_head = new_head.next
            old_head = old_head.next
        return visited[head]

    def copyRandomList3(self, head):
        if not head:return
        #时间复杂度O(n) 空间复杂度O(1)
        cur = head
        while cur:
            node = ListNode(cur.value,True)
            cur.next, node.next, cur = node, cur.next,cur.next
        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next
        old_head, new_head, ret = head, head.next, head.next
        while old_head:
            old_head.next = old_head.next.next if old_head.next else None
            new_head.next = new_head.next.next if new_head.next else None
            new_head = new_head.next
            old_head = old_head.next
        return ret
if __name__=='__main__':
    s =Solution()
    head = create_listnode([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    print('1',s.copyRandomList(head))
    print('2', s.copyRandomList2(head))
    print('3', s.copyRandomList3(head))
