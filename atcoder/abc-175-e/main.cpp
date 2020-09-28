#include <bits/stdc++.h>

using namespace std;

int main()
{
    int R, C, K;
    cin >> R >> C >> K;
    vector<vector<int>> maap(R, vector<int>(C, 0));
    for(int i=0; i<K; i++){
        int r, c, v;
        cin >> r >> c >> v;
        maap[r-1][c-1] = v;
    }
    vector<vector<vector<long long>>> dp(R, vector<vector<long long>>(C, vector<long long>(4, 0)));
    if(maap[0][0])
        dp[0][0][1] = maap[0][0];
        
    for(int i=1; i<C; i++){
        dp[0][i][0] = dp[0][i-1][0];
        if(maap[0][i]){
            dp[0][i][1] = max(dp[0][i-1][1], dp[0][i-1][0] + maap[0][i]);
            dp[0][i][2] = max(dp[0][i-1][2], dp[0][i-1][1] + maap[0][i]);
            dp[0][i][3] = max(dp[0][i-1][3], dp[0][i-1][2] + maap[0][i]);
        }
        else{
            dp[0][i][1] = dp[0][i-1][1];
            dp[0][i][2] = dp[0][i-1][2];
            dp[0][i][3] = dp[0][i-1][3];
        }
    }
    for(int i=1; i<R; i++){
        dp[i][0][0] = max({dp[i-1][0][0], dp[i-1][0][1], dp[i-1][0][2], dp[i-1][0][3]});
        if(maap[i][0]){
            dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][0][0] + maap[i][0]);
            dp[i][0][2] = max(dp[i-1][0][2], dp[i-1][0][1] + maap[i][0]);
            dp[i][0][3] = max(dp[i-1][0][3], dp[i-1][0][2] + maap[i][0]);
        }
        else{
            dp[i][0][1] = dp[i-1][0][1];
            dp[i][0][2] = dp[i-1][0][2];
            dp[i][0][3] = dp[i-1][0][3];
        }
    }
    
    for(int r=1; r<R; r++){
        for(int c=1; c<C; c++){
            dp[r][c][0] = max({dp[r-1][c][0], dp[r-1][c][1], dp[r-1][c][2], dp[r-1][c][3],
                        dp[r][c-1][0]});
            
            if(maap[r][c]){
                dp[r][c][1] = max({
                    dp[r-1][c][0] + maap[r][c],
                    dp[r-1][c][1] + maap[r][c],
                    dp[r-1][c][2] + maap[r][c],
                    dp[r-1][c][3] + maap[r][c],
                    dp[r][c-1][0] + maap[r][c],
                    dp[r][c-1][1]
                });
                
                dp[r][c][2] = max({
                    dp[r][c-1][1] + maap[r][c],
                    dp[r][c-1][2],
                    // dp[r-1][c][1] + maap[r][c],
                    // dp[r-1][c][2]
                });
                dp[r][c][3] = max({
                    dp[r][c-1][2] + maap[r][c],
                    dp[r][c-1][3],
                    // dp[r-1][c][2] + maap[r][c],
                    // dp[r-1][c][3]
                });
            }
            else{
                dp[r][c][1] = dp[r][c-1][1];
                dp[r][c][2] = dp[r][c-1][2];
                dp[r][c][3] = dp[r][c-1][3];
            }
        }
    }
    cout << max({dp[R-1][C-1][3], dp[R-1][C-1][2], dp[R-1][C-1][1], dp[R-1][C-1][0]}) << '\n';
    return 0;
}
