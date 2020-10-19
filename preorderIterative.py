# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        
        travStack,res=[root],[]
        
        while travStack:
            current = travStack.pop()
            res.append(current.val)
            if current.right is not None:
                travStack.append(current.right)
            if current.left is not None:
                travStack.append(current.left)
            
        return res
            
        
        