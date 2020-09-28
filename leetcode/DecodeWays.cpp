class Solution {
public:
    int go(string &s, int n, vector<int>& memo){
        if(n == s.size()-1){
            if(s[n] == '0')
                memo[n] = 0;
            else
                memo[n] = 1;
            return memo[n];
        }
        if(n == s.size()-2){
            if(1 <= stoi(s.substr(n, 2)) && stoi(s.substr(n, 2)) <= 26
               && s.substr(n, 2) != "10" && s.substr(n, 2) != "20")
                memo[n] = 2;
            else
                memo[n] = 1;
            return memo[n];
        }
        if(memo[n])
            return memo[n];
        
        if(n <= memo.size()-2 && 1 <= stoi(s.substr(n, 2)) && stoi(s.substr(n, 2)) <= 26 
          && s.substr(n, 2) != "10" && s.substr(n, 2) != "20"){
            int tmp;
            tmp = go(s, n+1, memo) + go(s, n+2, memo);
            memo[n] = tmp;
            return memo[n];
        } 
        else if(n <= memo.size()-2 && 1 <= stoi(s.substr(n, 2)) && stoi(s.substr(n, 2)) <= 26 
          && (s.substr(n, 2) == "10" || s.substr(n, 2) == "20")){
              memo[n] = go(s, n+2, memo);
              return memo[n];
          }
        else{
            memo[n] = go(s, n+1, memo);
            return memo[n];
        }
    }
    
    int numDecodings(string s) {
        if(s == "0")
            return 0;
        for(int i=0; i<s.size(); i++){
            if(s[i] == '0'){
                if(i > 0 && (s[i-1] == '1' || s[i-1] == '2'))
                    continue;
                else
                    return 0;
            }
        }
        int n = s.size();
        vector<int> memo(n, 0);
        return go(s, 0, memo);
    }
};
