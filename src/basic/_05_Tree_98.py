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
from src.common.tree import create_treenode
class Solution:
    def inorder(self, root):
        # O(n)
        if root is None:
            return []
        return self.inorder(root.left) + [root.value]+self.inorder(root.right)

    def isValidBST1(self, root) -> bool:
        inorder = self.inorder(root)
        return inorder == list(sorted(set(inorder)))

    def helper(self, root):
        if root is None:
            return True
        if not self.helper(root.left):
            return False
        if self.prev and self.prev.value >= root.value:
            return False
        self.prev = root
        return self.helper(root.right)

    def isValidBST2(self, root) -> bool:  # 递归中序遍历
        self.prev = None
        # O(n)
        return self.helper(root)

    def is_bst(self, root, min_value=float('-inf'), max_value=float('inf')):
        if root is None:
            return True
        return (min_value < root.value < max_value
                and self.is_bst(root.left, min_value, root.value)
                and self.is_bst(root.right, root.value, max_value))

    def isValidBST3(self, root) -> bool:  # 递归
        # O(n)
        return self.is_bst(root, float('-inf'), float('inf'))

    def isValidBST4(self, root) -> bool:  # 迭代中序遍历
        stack = []
        node = root
        inorder = float('-inf')
        #O(n*n)
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.value <= inorder:
                return False
            inorder = node.value
            node = node.right
        return True


if __name__ == "__main__":
    tree_node = create_treenode([2, 1, 3])
    s = Solution()
    print('1', s.isValidBST1(tree_node))
    print('2', s.isValidBST2(tree_node))
    print('3', s.isValidBST3(tree_node))
    print('4', s.isValidBST4(tree_node))
    tree_node = create_treenode([5, 1, 4, None, None, 3, 6])
    print('1', s.isValidBST1(tree_node))
    print('2', s.isValidBST2(tree_node))
    print('3', s.isValidBST3(tree_node))
    print('4', s.isValidBST4(tree_node))
