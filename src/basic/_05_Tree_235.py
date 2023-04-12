'''
235. 二叉搜索树的最近公共祖先
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
示例 1:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。
示例 2:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉搜索树中。
'''
from common.tree import create_treenode


class Solution:
    def lowestCommonAncestor1(self, root, p, q):
        #O(n)
        if p.value < root.value > q.value:
            root = self.lowestCommonAncestor1(root.left, p, q)
        if p.value > root.value < q.value:
            root = self.lowestCommonAncestor1(root.right, p, q)
        return root

    def lowestCommonAncestor2(self, root, p, q):
        #O(n)
        while root:
            if p.value < root.value > q.value:
                root = root.left
            elif p.value > root.value < q.value:
                root = root.right
            else:
                return root


if __name__ == "__main__":
    s = Solution()
    tree_node = create_treenode([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = create_treenode([2, 8, 0, 4, 7, 9, None, None, 3, 5])
    q = create_treenode([8, 0, 4, 7, 9, None, None, 3, 5])
    print('1', s.lowestCommonAncestor1(tree_node, p, q).value)
    print('2', s.lowestCommonAncestor2(tree_node, p, q).value)
    tree_node = create_treenode([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = create_treenode([2])
    q = create_treenode([4])
    print('1', s.lowestCommonAncestor1(tree_node, p, q).value)
    print('2', s.lowestCommonAncestor2(tree_node, p, q).value)
