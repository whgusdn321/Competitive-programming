class Solution {
public:
    void print(vector<vector<int>> &vecs){
        for(auto vec : vecs){
            cout << "min : " << vec[0] << " value : " << vec[1] << " sum by far : " << vec[2] << " cnt : " << vec[3] << '\n';
        }
        cout << '\n';
    }
    int maxProfit(int k, vector<int>& prices) {
        int n = prices.size();
        if( n == 0 || k == 0)
            return 0;
        
        if (2*k >= n){
            int ans = 0;
            for(int i=0; i<n-1; i++){
                if(prices[i] < prices[i+1])
                    ans += prices[i+1] - prices[i];
            }
            return ans;
        }
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(k+1, vector<int>(2, 0))); // dp[n][k+1][2];
        dp[0][0][0] = 0;
        dp[0][0][1] = -prices[0];
        for(int i=1; i<k+1; i++)
            dp[0][i][1] = -prices[0];
        
        for(int i=1; i<n; i++){
            for(int j=0; j<k+1; j++){
               if(j > 0)
                   dp[i][j][0] = max(dp[i-1][j-1][1] + prices[i], dp[i-1][j][0]);
               dp[i][j][1] = max(dp[i-1][j][0] - prices[i], dp[i-1][j][1]);
                
            }
        }
        int ans = 0;
        for(int j=0; j <=k; j++){
            ans = max(ans, dp[n-1][j][0]);
        }
        return ans;
        
    }
};
