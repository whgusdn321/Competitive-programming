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
    int go(TreeNode *node, int val){
        if(node == NULL)
            return val;
        
        int a = go(node->right, val);    
        node->val += a;
        int b = go(node->left, node->val);
        return b;
    }
    
    TreeNode* bstToGst(TreeNode* root) {
        int last = go(root, 0);
        return root;
    }
};
