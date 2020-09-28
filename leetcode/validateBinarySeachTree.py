# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node: TreeNode) -> bool:
        
        if node.left and node.right:
            lmin, lmax = self.dfs(node.left)
            rmin, rmax = self.dfs(node.right)
            if lmax < node.val < rmin:
                return (lmin, rmax)
            else:
                return (-2e11, 2e11)
        
        elif node.left:
            lmin, lmax = self.dfs(node.left)
            if lmax < node.val:
                return (lmin, node.val)
            else:
                return (-2e11, 2e11)
        elif node.right:
            rmin, rmax = self.dfs(node.right)
            if node.val < rmin:
                return (node.val, rmax)
            else:
                return (-2e11, 2e11)
        else:
            return (node.val, node.val)
    
    def isValidBST(self, rootNode):
        if not rootNode:
            return True 
        x = self.dfs(rootNode)
        if x != (-2e11, 2e11):
            print(x)
            return True
        else:
            return False
