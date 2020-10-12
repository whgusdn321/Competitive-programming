class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> a = {0, 1};
        //int last = 1;
        while(a.size() - 1 < num){
            int n = a.size();
            for(int i=0; i<n; i++){
                a.push_back(a[i] + 1);
            }
        }
        vector<int> ans(a.begin(), a.begin()+num+1);
        return ans;
    }
};
