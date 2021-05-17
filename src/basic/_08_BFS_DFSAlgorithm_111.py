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
from src.common.tree import create_treenode
class Solution:
    def minDepth(self, root) -> int:
        if not root:return 0
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        return left_depth+right_depth+1 if (left_depth == 0 or right_depth == 0) else min(left_depth, right_depth)+1
    def maxDepth(self, root) -> int:
        if not root:return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
if __name__ == "__main__":
    s = Solution()
    l = [3, 9, 20, None, None, 15, 7]
    t = create_treenode(l)
    print(t)
    print('1', s.minDepth(t))
    print('2', s.maxDepth(t))