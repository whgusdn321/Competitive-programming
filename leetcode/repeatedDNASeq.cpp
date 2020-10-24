class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        unordered_map<string, int> dict;
        vector<string> ans;
        if(s.size() < 10)
            return ans;
        
        string tmp = s.substr(0, 10);
        dict[tmp] += 1;
        for(int i=10; i<s.size(); i++){
            tmp = tmp.substr(1, 9);
            tmp += s[i];
            dict[tmp] += 1;
        }
        for(auto it=dict.begin(); it!=dict.end(); it++){
            if(it->second > 1)
                ans.push_back(it->first);
        }
        return ans;
    }
};
