class Solution(object):
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while(True):
            while root is not None:
                stack.append(root)
                root=root.left
            root = stack.pop()
            k-=1
            if k==0:
                return root.val
            root =root.right