class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if(digits == "")
            return {};
        vector<vector<char>> vec(10, vector<char>(0));
        for(char x : "abc")
            vec[2].push_back(x);
        for(char x:"def")
            vec[3].push_back(x);
        for(char x:"ghi")
            vec[4].push_back(x);
        for(char x: "jkl")
            vec[5].push_back(x);
        for(char x: "mno")
            vec[6].push_back(x);
        for(char x: "pqrs")
            vec[7].push_back(x);
        for(char x: "tuv")
            vec[8].push_back(x);
        for(char x: "wxyz")
            vec[9].push_back(x);
        for(int i=2; i<10; i++)
            vec[i].pop_back();
        vector<string> ans;
        ans.push_back("");
        for(char x:digits){
            vector<string> nxt;
            for(string t : ans){
                //cout << "t is : " << t << " x is : " << x << '\n';
                for(char xx:vec[x-'0']){
                    nxt.push_back(t+xx);
                }
            }
            ans = nxt;
        }
        //ans.erase(ans.begin());
        return ans;
    }
};
