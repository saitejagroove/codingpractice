# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        if root is None:
            return
        
        if (root.left is None) and (root.right is None):
            if (sum - root.val) ==0 :
                return True
        
        if(self.hasPathSum(root.left,sum-root.val)):
            return True
        if (self.hasPathSum(root.right,sum-root.val)):
            return True