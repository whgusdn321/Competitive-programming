#include <bits/stdc++.h>

using namespace std;

int go(int n, vector<int> &s, vector<int> &dp){
    if(n < 1){
        return 0;
    }
    if(n == 1){
        return 1;
    }
    
    if(dp[n] != -1)
        return dp[n];
    else{
        int tmp = 0;
        for(int ss : s){
            tmp += go(n - ss, s, dp);
            tmp %= 998244353;
        }
        dp[n] = tmp;
        return dp[n];
    }
}
int main()
{
    int n, k;
    int l, r;
    cin >> n >> k;
    vector<int> s;
    for(int i=0; i<k; i++){
        cin >> l >> r;
        for(int j=l; j<=r; j++){
            s.push_back(j);
        }
    }
    vector<int> dp(n+1, -1);
    dp[1] = 1;
    int ans = go(n, s, dp);
    cout << ans << '\n';
    return 0;
}

