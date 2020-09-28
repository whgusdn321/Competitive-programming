const int ALPHABET_SIZE = 26;

int dy[4] = {1, 0, -1, 0};
int dx[4] = {0, -1, 0, 1};

class Solution {
public:
    // trie node 
    struct TrieNode 
    { 
        struct TrieNode *children[ALPHABET_SIZE]; 
      
        // isEndOfWord is true if the node represents 
        // end of a word 
        bool isEndOfWord; 
    }; 
      
    // Returns new trie node (initialized to NULLs) 
    struct TrieNode *getNode(void) 
    { 
        struct TrieNode *pNode =  new TrieNode; 
      
        pNode->isEndOfWord = false; 
      
        for (int i = 0; i < ALPHABET_SIZE; i++) 
            pNode->children[i] = NULL; 
      
        return pNode; 
    } 
      
    // If not present, inserts key into trie 
    // If the key is prefix of trie node, just 
    // marks leaf node 
    void insert(struct TrieNode *root, string key) 
    { 
        struct TrieNode *pCrawl = root; 
      
        for (int i = 0; i < key.length(); i++) 
        { 
            int index = key[i] - 'a'; 
            if (!pCrawl->children[index]) 
                pCrawl->children[index] = getNode(); 
      
            pCrawl = pCrawl->children[index]; 
        } 
      
        // mark last node as leaf 
        pCrawl->isEndOfWord = true; 
    } 
      
    // Returns true if key presents in trie, else 
    // false 
    bool search(struct TrieNode *root, string key) 
    { 
        struct TrieNode *pCrawl = root; 
      
        for (int i = 0; i < key.length(); i++) 
        { 
            int index = key[i] - 'a'; 
            if (!pCrawl->children[index]) 
                return false; 
      
            pCrawl = pCrawl->children[index]; 
        } 
      
        return (pCrawl != NULL && pCrawl->isEndOfWord); 
    } 
    unordered_map<string, bool> dict;
    vector<string> rets;
    int h, w;
    
    void dfs(struct TrieNode *node, int y, int x, vector<vector<char>> &board, string ret, vector<vector<bool>> &visited){
        if(node->isEndOfWord){
            rets.push_back(ret);
        }
        
        
        for(int i=0; i<4; i++){
            int ny = y + dy[i];
            int nx = x + dx[i];
            if(0<=ny && ny < h && 0<= nx && nx < w && node->children[board[ny][nx]-'a'] 
              && !visited[ny][nx]){
                visited[ny][nx] =true;
                dfs(node->children[board[ny][nx]-'a'], ny, nx, board, ret+board[ny][nx], visited);
                visited[ny][nx] = false;
            }
        }
        
        return;
    }
    
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {

        map<char, bool> start;
        h = board.size();
        w = board[0].size();
        struct TrieNode *root = getNode();
        vector<vector<bool>> visited(h, vector<bool>(w, false));
        for(string word : words){
            start[word[0]] = true;
            insert(root, word);
            dict[word] = true;
        }
        
        for(int i=0; i<h; i++){
            for(int j=0; j<w; j++){
                if(start[board[i][j]]){
                    //cout <<board[i][j] << '\n';
                    string s = "";
                    visited[i][j] = true;
                    dfs(root->children[board[i][j]-'a'], i, j, board, s+board[i][j], visited);
                    visited[i][j] = false;
                }
            }
        }
        vector<string> ans;
        for(string ret : rets){
            if(dict[ret]){
                ans.push_back(ret); 
                dict[ret] = false;
            }
        }
        return ans;
    }
};
