'''
面试题34. 二叉树中和为某一值的路径
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
示例:
给定如下二叉树，以及目标和 target = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
 

提示：

节点总数 <= 10000
'''


class Solution:
    def pathSum(self, root, target: int):
        if not root:return []
        #时间复杂度O(n^2) 空间复杂度O(n)
        def dfs(node, target):
            if not node:return
            path.append(node.value)
            target -=node.value
            if not node.left and not node.right and target == 0:
                ret.append(path[:])
            dfs(node.left, target)
            dfs(node.right, target)
            path.pop()
            
        ret =[]
        path=[]
        dfs(root, target)
        return ret
if __name__ =='__main__':
    s = Solution()
    from src.common.tree import create_treenode
    root = create_treenode(
        [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None,5, 1])
    target = 22
    print(root)
    print('1',s.pathSum(root,target))
