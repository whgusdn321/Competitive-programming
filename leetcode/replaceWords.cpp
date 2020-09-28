const int ALPHABET_SIZE = 26; 
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
    struct TrieNode* getNode(void) 
    { 
        struct TrieNode *pNode = new TrieNode; 
      
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
            // pCrawl->cnt[key.length()] += 1;
        } 
      
        // mark last node as leaf 
        pCrawl->isEndOfWord = true; 
    } 
      
    // Returns true if key presents in trie, else 
    // false 
    string search(struct TrieNode *root, string key) 
    {    
        struct TrieNode *pCrawl = root; 
        string ret = "";
        for (int i = 0; i < key.length(); i++) 
        { 
            int index = key[i] - 'a'; 
            if (!pCrawl->children[index]) 
                return key; 
             
            ret += key[i];
            pCrawl = pCrawl->children[index]; 
            if(pCrawl->isEndOfWord)
                break;
        } 
        return ret;
        // return (pCrawl != NULL && pCrawl->isEndOfWord); 
    } 
    
    string replaceWords(vector<string>& dictionary, string sentence) {
        struct TrieNode *root = getNode();
        vector<string> vec;
        istringstream iss(sentence);
        vector<string> results((istream_iterator<string>(iss)), istream_iterator<string>());
        string ans;
        for(string word : dictionary){
            insert(root, word);
        }
        for(string word : results){
            string tmp = search(root, word);
            ans += tmp;
            ans += ' ';
        }
        return ans.substr(0, ans.size()-1);
    }
};
