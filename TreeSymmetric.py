# Definition for a binary tree node. Symmetry Check
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        if root.left is None and root.right is None:
            return True
        if root.left is None or root.right is None or (root.left).val!=(root.right).val:
            return False
        leftlist,rightlist=[],[]
        
        def preOrdTrav(node):
            if node is None:
                return
            else:
                if (node.left is None):
                    if (node.right is not None):
                        leftlist.append(None)
                    
                preOrdTrav(node.left)
                leftlist.append(node.val)
                if (node.left is not None):
                    if (node.right is None):
                        leftlist.append(None)
                preOrdTrav(node.right)
                
            return
        def revPreOrdTrav(node):
            if node is None:
                return
            else:
                if (node.right is None):
                    if (node.left is not None):
                        rightlist.append(None)
                revPreOrdTrav(node.right)
                rightlist.append(node.val)
                if (node.right is not None):
                    if (node.left is None):
                        rightlist.append(None)
                revPreOrdTrav(node.left)
            return
        preOrdTrav(root.left)
        revPreOrdTrav(root.right)
        if leftlist!= rightlist:
            return False
        return True
            