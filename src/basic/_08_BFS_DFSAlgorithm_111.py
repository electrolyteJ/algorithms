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
    def minDepth1(self, root) -> int:
        if not root:
            return 0
        left_depth = self.minDepth1(root.left)
        right_depth = self.minDepth1(root.right)
        return left_depth+right_depth+1  if (left_depth == 0 or right_depth == 0) else min(left_depth, right_depth)+1
    def minDepth2(self, root) -> int:
         pass
    def maxDepth1(self, root) -> int:
        pass
    def maxDepth2(self, root) -> int:
        if not root:return 0
        return max(self.maxDepth2(root.left),self.maxDepth2(root.right))+1


if __name__ == "__main__":
    s = Solution()
    l = [3, 9, 20, None, None, 15, 7]
    t = create_treenode(l)
    print(t)
    print('1', s.minDepth1(t))
    print('2', s.maxDepth2(t))
    # l = [2, None, 3, None, 4, None, 5, None, 6]
    # t = create_treenode(l)
    # print(t)
    # print('1', s.minDepth1(t))
    # print('2', s.minDepth2(t))
