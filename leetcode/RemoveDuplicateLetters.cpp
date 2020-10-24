class Solution {
public:
    string removeDuplicateLetters(string s) {
        bool vi[26];
        int arr[26];
        stack<char> stk;
        int n = s.size();
        fill(vi, vi+26, false);
        fill(arr, arr+26, false);
        
        for(int i=0; i<n; i++){
            arr[s[i]-'a'] = i;
        }
        
        for(int i=0; i<n; i++){
            if(!vi[s[i]-'a']){
                while(!stk.empty() && stk.top() > s[i] && arr[stk.top()-'a'] > i){
                    vi[stk.top()-'a'] = false;
                    stk.pop();
                }
                stk.push(s[i]);
                vi[s[i]-'a'] = true;
            }
        }
        string ans;
        while(!stk.empty()){
            ans += stk.top();
            stk.pop();
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
