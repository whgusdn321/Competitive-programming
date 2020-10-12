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
class BSTIterator {
public:
    stack<int> stakk;
    BSTIterator(TreeNode* root) {
        dfs(root);
    }
    void dfs(TreeNode *node){
        if(node == NULL)
            return;
        dfs(node->right);   
        stakk.push(node->val);
        dfs(node->left);
    }
    /** @return the next smallest number */
    int next() {
        int t = stakk.top();
        stakk.pop();
        return t;
    }
    
    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !stakk.empty();
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
