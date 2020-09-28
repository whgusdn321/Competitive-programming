class Solution {
public:
    int maximalSquare(vector<vector<char>>& mp) {
        int n = mp.size();
        if(n==0)
            return 0;
        
        int m = mp[0].size();
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(m, vector<int>(2, 0)));
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(mp[i][j] == '1'){
                    dp[i][j][0] = mp[i][j] - '0';
                    dp[i][j][1] = mp[i][j] - '0';
                    if(j-1 >= 0)
                        dp[i][j][0] += dp[i][j-1][0];
                    if(i-1 >= 0)
                        dp[i][j][1] += dp[i-1][j][1];
                } 
            }
        }
        
        vector<pair<int, int>> starts;
        for(int i=0; i<n; i++){
            starts.push_back({i, 0});
        }
        for(int j=0; j<m; j++){
            starts.push_back({0, j});
        }
        int ans = 0;
        for(auto t:starts){
            int y = t.first;
            int x = t.second;
            int num = 1;
            while(y<n && x <m){
                if(dp[y][x][0] >= num && dp[y][x][1] >= num){
                    ans = max(ans, num);
                    num++;
                }
                else{
                    num = min(dp[y][x][0], dp[y][x][1]);
                    num++;
                }
                y++;
                x++;
            }   
        }
        return ans*ans;
    }
    
};
