class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        output =[]
        
        if root is None:
            return []
        
        output = output + self.postorderTraversal(root.left)
        output = output + self.postorderTraversal(root.right)
        output.append(root.val)
        
        return output
