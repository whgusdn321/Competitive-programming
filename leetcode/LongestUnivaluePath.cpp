/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int ans = 0;
    
    int f(TreeNode * me, int pval){
        if(me == NULL)
            return 0;
        
        int l = f(me->left, me->val);
        int r = f(me->right, me->val);
        ans = max(ans, l+r);
        if(me->val == pval)
            return max(l, r) + 1;
        else
            return 0;
    }
    
    int longestUnivaluePath(TreeNode* root) {
        f(root, 999);
        return ans;
    }
};
