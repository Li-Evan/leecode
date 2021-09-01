''''''
'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 中序遍历且递归，极慢
# class Solution:
#     def __init__(self):
#         self.li = []
#     def isValidBST(self, root) -> bool:
#         if not root:
#             return True
#         self.isValidBST(root.left)
#         self.li.append(root.val)
#         self.isValidBST(root.right)
#
#         for i in range(len(self.li)-1):
#             if self.li[i] >= self.li[i+1]:
#                 return False
#         return True




class Solution:
    def isValidBST(self, root) -> bool:
        x = root.val
        if not root:
            return True
        if not root.left and not root.right:
            return True
        while True:
            if root.left:
                if root.left.val >= x:
                    return False
                else:
                    root = root.left
