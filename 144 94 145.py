'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
'''

'''
递归算法
非常简单 左就是preorderTraversal（self.left），右就是preorderTraversal（self.right），根就是print（self.val）
前序就是根左右 中序就是左根右 后序就是左右根
'''

# 前序
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# class Solution:
#     def __init__(self):
#         super().__init__
#         self.li = []
#
#     def preorderTraversal(self, root: TreeNode):
#         if root == None:
#             return []
#         self.li.append(root.val)
#         self.preorderTraversal(root.left)
#         self.preorderTraversal(root.right)
#         return self.li

# 中序
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        super().__init__
        self.li = []

    def inorderTraversal(self, root: TreeNode):
        if root == None:
            return []
        self.inorderTraversal(root.left)
        self.li.append(root.val)
        self.inorderTraversal(root.right)
        return self.li

# 后序
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# class Solution:
#     def __init__(self):
#         super().__init__
#         self.li = []
#
#     def postorderTraversal(self, root: TreeNode):
#         if root == None:
#             return []
#         self.postorderTraversal(root.left)
#         self.postorderTraversal(root.right)
#         self.li.append(root.val)
#         return self.li