'''
剑指 Offer 54. 二叉搜索树的第k大节点
给定一棵二叉搜索树，请找出其中第k大的节点。

示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
限制：
1 ≤ k ≤ 二叉搜索树元素个数
'''
class Solution:
    def kthLargest(self, root, k: int) -> int:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left)+[node.value] + inorder(node.right)
        return inorder(root)[-k]

if __name__ == '__main__':
        s = Solution()
        from common.tree  import create_treenode
        root = create_treenode([3, 1, 4, None, 2])
        k=1
        print(s.kthLargest(root,k))
        root = create_treenode([5, 3, 6, 2, 4, None, None, 1])
        k=3
        print(s.kthLargest(root,k))
