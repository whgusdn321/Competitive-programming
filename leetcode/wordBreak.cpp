class Solution {
public:
    bool go(string &s, int i, vector<int> &memo, vector<string> &wordDict){
        if(i == s.size()){
            return true;
        } 
        if(memo[i] != -1){
            if(memo[i] == 0)
                return false;
            else
                return true;
        }
        
        bool pos = false;
        for(string word : wordDict){
            int len = word.size();
            if(i+len <= s.size() && s.substr(i, len) == word){
                pos |= go(s, i+len, memo, wordDict);
            }
        }
        if(pos)
            memo[i] = 1;
        else
            memo[i] = 0;
        return pos;
    }
    
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<int> memo(s.size(), -1);    
        go(s, 0, memo, wordDict);
        if(memo[0] == 0) // not possible
            return false;
        else
            return true;
    }
};
