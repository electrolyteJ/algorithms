'''
102. 二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：

[
  [3],
  [9,20],
  [15,7]
'''


from mock.tree import create_treenode


class Solution:
    def levelOrder1(self, root):
        pass
    def levelOrder2(self, root):
        pass


if __name__ == "__main__":
    s = Solution()
    l = [3, 9, 20, None, None, 15, 7]
    print('1', s.levelOrder1(create_treenode(l)))
    print('1', s.levelOrder2(create_treenode(l)))
