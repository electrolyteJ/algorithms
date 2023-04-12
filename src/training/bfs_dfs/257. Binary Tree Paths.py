'''
257. 二叉树的所有路径
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
'''


class Solution:
    def binaryTreePaths(self, root):
        if not root:return []
        def dfs(node,path):
            if not node:return
            path += str(node.value)
            if not node.left and not node.right:
                paths.append(path)
            else:
                path +='->'
                dfs(node.left, path)
                dfs(node.right, path)
        paths=[]
        dfs(root,'')
        return paths
if __name__ =='__main__':
    s =Solution()
    from common.tree import create_treenode
    root = create_treenode([1,2,3,None,5])
    print(root)
    print('1',s.binaryTreePaths(root))
