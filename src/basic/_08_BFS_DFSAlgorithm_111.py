'''
111. 二叉树的最小深度
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。

 

示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：2
示例 2：

输入：root = [2,null,3,null,4,null,5,null,6]
输出：5
'''

from mock.tree import create_treenode
class Solution:
    def minDepth(self, root) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    l = [3, 9, 20, None, None, 15, 7]
    print('1', s.minDepth(create_treenode(l)))
    l = [2, None, 3, None, 4, None, 5, None 6]
    print('1', s.minDepth(create_treenode(l)))
