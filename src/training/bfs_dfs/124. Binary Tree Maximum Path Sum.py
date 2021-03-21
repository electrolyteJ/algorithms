'''
124. 二叉树中的最大路径和
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。

示例 1：

输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
示例 2：

输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42

提示：

树中节点数目范围是 [1, 3 * 104]
-1000 <= Node.val <= 1000
'''

from src.common.tree import create_treenode
class Solution:
    def maxPathSum(self, root) -> int:
        def maxGain(node):
            if not node:
                return 0
            left_gain=max(maxGain(node.left),0)
            righ_gain=max(maxGain(node.right),0)
            price_new_path=node.value+righ_gain+left_gain
            self.max_gain = max(self.max_gain, price_new_path)
            return node.value +max(left_gain,righ_gain)
        #时间复杂度O(n) 空间复杂度O(n)
        self.max_gain=float('-inf')
        maxGain(root)
        return self.max_gain
if __name__ =='__main__':
    s = Solution()
    root = create_treenode([1,2,3])
    print(root)
    print('1',s.maxPathSum(root))
    root = create_treenode([-10, 9, 20, None, None, 15, 7])
    print(root)
    print('1',s.maxPathSum(root))
    root = create_treenode([-3])
    print(root)
    print('1',s.maxPathSum(root))
