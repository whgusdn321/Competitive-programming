class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size() == 0)
            return "";
        
        string ret = strs[0];
        for(string s : strs){
            int cnt = 0;
            for(int i=0; i<ret.size(); i++){
                if(ret[i] == s[i])
                    cnt++;
                else
                    break;
            }
            ret = ret.substr(0, cnt);
        }
        return ret;
    }
};
