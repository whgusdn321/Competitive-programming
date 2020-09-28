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
    vector<int> inorderTraversal(TreeNode* root) {
        TreeNode *cur = root;
        vector<int> ret;
        stack<TreeNode*> stakk;
        map<TreeNode*, bool> visited;
        
        while(cur!=NULL){
            while(cur->left != NULL && !visited[cur->left]){
                stakk.push(cur);
                cur = cur->left;
                visited[cur] = true;
            }
            
            ret.push_back(cur->val);
            visited[cur] = true;
            
            if(cur->right != NULL){
                cur = cur->right;
            }
            else{
                if(stakk.empty()){
                    cur = NULL;
                }
                else{
                    cur = stakk.top();
                    stakk.pop();
                }
            }
            
        }
        return ret;
    }
};
