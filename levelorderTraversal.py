# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue =[]
        out = []
        
        if root is None:
            return queue
        queue.append([root])
        i=0
        while(queue):
            q2= queue.pop(0)
            temp=[]
            res=[]
            
            while(q2):
                curr = q2.pop(0)
                res.append(curr.val)
                if curr.left is not None: 
                    temp.append(curr.left)
                if curr.right is not None:
                    temp.append(curr.right)
            out.append(res)
            if(temp!=[]):
                queue.append(temp)
            
            
        return out