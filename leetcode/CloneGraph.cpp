/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    void dfs(Node* p, Node* p_cpd, vector<Node*>& visited){
        for(Node* child : p->neighbors){
            if(!visited[child->val]){
                Node* child_cpd = new Node(child->val);
                visited[child->val] = child_cpd;
                dfs(child, child_cpd, visited);
                p_cpd->neighbors.push_back(child_cpd); 
            }
            else{
                p_cpd->neighbors.push_back(visited[child->val]);
            }
        }
    }
    Node* cloneGraph(Node* node) {
        if(!node)
            return node;
        
        vector<Node*> vis(101, NULL);
        Node* rootNode = new Node(node->val);
        vis[rootNode->val] = rootNode;
        
        for(Node* child : node->neighbors){
            if(!vis[child->val]){
                Node* newNode = new Node(child->val);
                vis[newNode->val] = newNode;
                dfs(child, newNode, vis);
                rootNode->neighbors.push_back(newNode);
            }
            else{
                rootNode->neighbors.push_back(vis[child->val]);
            }
        }
        cout << rootNode->val << '\n';
        
        //cout<< a.val <<'\n';
        return rootNode;
    }
};
