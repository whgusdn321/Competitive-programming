class Solution {
public:
    int dp[50];
    int climbStairs(int n) {
        if(n==0) return 1;
        if(n < 0) return 0;
        if(dp[n])
            return dp[n];
        else{
            dp[n] = climbStairs(n-1) + climbStairs(n-2);
            return dp[n];
        }
    }
};
