"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
Example 1:
Input: root = [4,2,6,1,3]
Output: 1
Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1
Constraints:
The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105
"""

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []

        def depth(node):
            if node is None:
                return 
            values.append(node.val)
            depth(node.left)
            depth(node.right)
        
        depth(root)

        values.sort()
        mn = 1e9
        for i in range(1, len(values)):
            mn = min(mn, values[i]-values[i-1])
        
        return mn
