# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    res=0
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def checkUni(root):
            if root is None:
                return True
            
            if root.left is None and root.right is None:
                self.res+=1
                
                return True
            
            if (root.left is None):
                print("here")
                if checkUni(root.right) and (root.right).val == root.val:
                    self.res+=1
                    return True
            elif (root.right is None):
                print("here")
                if checkUni(root.left) and (root.left).val == root.val:
                    
                    self.res+=1
                    return True
            else:
                l= checkUni(root.left)
                r = checkUni(root.right)
                if l and r and (root.right).val == root.val and (root.left).val == root.val :
                    self.res+=1
                    return True
        
        checkUni(root)
        return self.res
            