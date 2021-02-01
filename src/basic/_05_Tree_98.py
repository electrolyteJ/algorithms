'''
98. 验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
'''
from mock.tree import TreeNode


class Solution:
    def inorder(self, root):
        # O(n)
        if root is None:
            return []
        return self.inorder(root.left) + [root.value]+self.inorder(root.right)

    def isValidBST1(self, root: TreeNode) -> bool:
        inorder = self.inorder(root)
        return inorder == list(sorted(set(inorder)))

    def isValidBST2(self, root: TreeNode) -> bool:
        pass

        pass


if __name__ == "__main__":
    tree_node = TreeNode.create([2, 1, 3])
    s = Solution()
    print(s.isValidBST1(tree_node))
