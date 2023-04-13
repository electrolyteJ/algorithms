'''
105. 从前序与中序遍历序列构造二叉树
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
'''
from common.tree import Node

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root_v = preorder[0]
        root_i = inorder.index(root_v)

        left = inorder[:root_i]
        left_subtree = self.buildTree(preorder[1:1+len(left)], left)
        right_subtree = self.buildTree(preorder[1+len(left):], inorder[1+root_i:])

        node = Node(root_v)
        node.left = left_subtree
        node.right = right_subtree

        return node

    def buildTree1(self, preorder, inorder):#递归
        #时间复杂度O(n) 空间复杂度O(n)
        def recur(preorder_s, preorder_e, inorder_s, inorder_e):
            if preorder_s > preorder_e:return
            num = preorder[preorder_s]
            inorder_m = indexs[num]
            l_len = inorder_m-inorder_s
            l_preorder_s, l_preorder_e = preorder_s+1, preorder_s+l_len
            l_inorder_s, l_inorder_e = inorder_s, inorder_m-1

            r_preorder_s, r_preorder_e = preorder_s+l_len+1, preorder_e
            r_inorder_s, r_inorder_e = inorder_m+1, inorder_e

            root = Node(num)
            root.left = recur(l_preorder_s, l_preorder_e,
                              l_inorder_s, l_inorder_e)
            root.right = recur(r_preorder_s, r_preorder_e,
                               r_inorder_s, r_inorder_e)
            return root
        m, n = len(preorder), len(inorder)
        indexs = {num: i for i, num in enumerate(inorder)}
        return recur(0, m-1, 0, n-1)

        

    def buildTree2(self, preorder, inorder):  # 迭代
        if not preorder:
            return None
        #时间复杂度O(n) 空间复杂度O(n)
        root = Node(preorder[0])
        stack = [root]
        inorderIndex = 0
        for i in range(1, len(preorder)):
            preorderVal = preorder[i]
            node = stack[-1]
            if node.value != inorder[inorderIndex]:
                node.left = Node(preorderVal)
                stack.append(node.left)
            else:
                while stack and stack[-1].value == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex += 1
                node.right = Node(preorderVal)
                stack.append(node.right)

        return root

if __name__ =='__main__':
    s = Solution()
    preorder = [3, 9, 20, 15, 7] #[根节点 [左子树] [右子树]]
    inorder = [9, 3, 15, 20, 7]  # [[左子树] 根节点 [右子树]]
    print('1', s.buildTree1(preorder,inorder))
    print('2', s.buildTree2(preorder, inorder))
