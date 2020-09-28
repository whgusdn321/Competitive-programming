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
    bool isSymmetric(TreeNode* root) {
        if(root == NULL)
            return true;
        queue<TreeNode*> qu;
        qu.push(root);
        bool pos = true;
        while(!qu.empty()){
            queue<TreeNode*> nqu;
            vector<int> v;
            while(!qu.empty()){
                TreeNode * n = qu.front();
                qu.pop();
                if(n->left != NULL)
                    nqu.push(n->left);
                if(n->right != NULL)
                    nqu.push(n->right);
                if(n->left == NULL)
                    v.push_back(-99999);
                else
                    v.push_back(n->left->val);
                if(n->right == NULL)
                    v.push_back(-99999);
                else
                    v.push_back(n->right->val);
            }
            vector<int> vv = v;
            reverse(v.begin(), v.end());
            if(vv == v){
                qu = nqu;
            }
            else{
                pos = false;
                break;
            }
        }
        return pos;
    }
};
