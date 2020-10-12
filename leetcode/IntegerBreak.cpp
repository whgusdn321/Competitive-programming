class Solution {
public:
    int memo[59];
    int nn;
    int go(int n){
        if(n==1)
            return 1;
        if(memo[n])
            return memo[n];
        int ret = 0;
        if(nn != n)
            ret = n;
        for(int k=1; k<n; k++){
            ret = max(ret, go(n-k)*k);
        }
        memo[n] = ret;
        return ret;
    }
    
    int integerBreak(int n) {
        nn = n;
        int ans = 0;
        ans = go(n);
        return ans;
    }
};
