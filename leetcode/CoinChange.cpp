class Solution {
public:
    int a = -100;
    int dp[10001];
    int go(vector<int>& coins, int amount, int cnt){
        if(amount < 0){
            return -1;
        }
        if(amount == 0){
            if(a == -100)
                a = cnt;
            return 0;
        }
        if(dp[amount] != -2){
            if(dp[amount] == -1)
                return -1;
            else
                return dp[amount] + 1;
        }
        
        dp[amount] = -1; // make visited
        for(int c : coins){
            int ret = go(coins, amount - c, cnt+1);
            if(ret >= 0)
                if(dp[amount] == -1)
                    dp[amount] = ret;
                else
                    dp[amount] = min(ret, dp[amount]); 
        }
        
        if(dp[amount] >= 0)
            return dp[amount] + 1;
        else
            return -1;
    }
    
    int coinChange(vector<int>& coins, int amount) {
        fill(dp, dp+10001, -2);
        sort(coins.begin(), coins.end(), greater<int>());
        int ans = go(coins, amount, 0);
        cout << a << '\n';
        return ans;
    }
};
