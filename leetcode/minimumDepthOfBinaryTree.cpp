class Solution {
public:
    int ans = 1e5;
    void go(TreeNode* node, int a){
        if(node->left==NULL && node->right==NULL){
            ans = min(ans, a);
            return;
        }
        if(node->left != NULL)
            go(node->left, a+1);
        if(node->right != NULL)
            go(node->right, a+1);
    }
    
    int minDepth(TreeNode* root) {
        if(root==NULL)
            return 0;
        go(root, 1);
        return ans;
    }
};
