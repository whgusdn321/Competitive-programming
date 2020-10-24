class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int p) {
        sort(tokens.begin(), tokens.end());
        int l = 0, r = tokens.size()-1;
        int s = 0;
        while(l<=r){
            if(tokens[l] <= p){
                p -= tokens[l];
                l++;
                s++;
            }
            else{
                if(p + tokens[r] >= tokens[l] && r != l && s > 0){
                    p += tokens[r];
                    r--;
                    s--;
                }
                else{
                    break;
                }
            }
        }
        return s;
    }
};
