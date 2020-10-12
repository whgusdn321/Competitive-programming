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
    vector<vector<int>> levelOrder(TreeNode* root) {
            
        queue<TreeNode*> qu;
        vector<vector<int>> ans;
        if(root==NULL)
            return ans;
        qu.push(root);
        while(!qu.empty()){
            queue<TreeNode*> nqu;
            vector<int> tmp;
            while(!qu.empty()){
                if(qu.front()->left != NULL)
                    nqu.push(qu.front()->left);
                if(qu.front()->right != NULL)
                    nqu.push(qu.front()->right);
                tmp.push_back(qu.front()->val);
                qu.pop();
            }
            ans.push_back(tmp);
            qu = nqu;
        }
        return ans;
    }
};
