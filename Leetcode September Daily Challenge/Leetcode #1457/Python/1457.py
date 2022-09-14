//Traverse all paths using dfs() function.
//Track count of digits in the path in counter list.
//Once a leaf is detected check if path is a pseudo-palindromic one. It is true only if counter has zero or one odd element(s).
//Time complexity = O(n), where n is a number of nodes in the tree
//Space complexity = O(h), where h is a height of the tree
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], counter: list[int]) -> int:
            counter[node.val-1] = 0 if counter[node.val-1] else 1
            if not (node.left or node.right):   # it is a leaf
                ret = 0 if sum(counter) > 1 else 1
            else:
                ret = 0
                if node.left:
                    ret = dfs(node.left, counter)
                if node.right:
                    ret += dfs(node.right, counter)
            counter[node.val-1] = 0 if counter[node.val-1] else 1
            return ret
                
        return dfs(root, [0] * 9)
