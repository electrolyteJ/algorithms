'''
236. 二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。
'''

from mock.tree import create_treenode


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root is None or p == root or q == root:
            return root
        left_subtree = self.lowestCommonAncestor(root.left, p, q)
        right_subtree = self.lowestCommonAncestor(root.right, p, q)
        if not left_subtree:
            return right_subtree
        else:
            if not right_subtree:
                return left_subtree
            else:
                return root


if __name__ == "__main__":
    s = Solution()
    tree_node = create_treenode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(tree_node)
    p = tree_node[1]
    q = tree_node[2]
    print(s.lowestCommonAncestor(tree_node, p, q).value)
    p = tree_node[1]
    q = tree_node[8]
    print(s.lowestCommonAncestor(tree_node, p, q).value)
