class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        vector<int> maxs(n, 0), mins(n, 0);
        int maxx = -1e9, minn = 1e9;
        for(int j=prices.size()-1; j>=0; j--){
            maxx = max(maxx, prices[j]);
            maxs[j] = maxx;
        }
        for(int i=0; i<n; i++){
            minn = min(minn, prices[i]);
            mins[i] = minn;
        }
        
        int ans = 0;
        for(int i=0; i<n; i++){
            int tmp = maxs[i] - mins[i];
            ans = max(ans, tmp);
        }
        return ans;
    }
};
