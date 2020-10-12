class Solution {
public:
    int dy[4] = {-1, 0, 1, 0};
    int dx[4] = {0, 1, 0, -1};
    
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        int h = matrix.size();
        int w = matrix[0].size();
        vector<vector<int>> ans(h, vector<int>(w, 0));
        vector<vector<bool>> vi(h, vector<bool>(w, false));
        
        queue<vector<int>> qu;
        for(int y=0; y<h; y++){
            for(int x=0; x<w; x++){
                if(matrix[y][x] == 0){
                    qu.push({y, x, 0});
                    vi[y][x] = true;
                }
            }
        }
        
        while(!qu.empty()){
            vector<int> tmp = qu.front();
            qu.pop();
            int y = tmp[0];
            int x = tmp[1];
            int cnt = tmp[2];
            ans[y][x] = cnt;  
            
            for(int i=0; i<4; i++){
                int ny = y + dy[i];
                int nx = x + dx[i];
                if(0<=ny && ny< h && 0<=nx && nx <w && !vi[ny][nx]){
                    qu.push({ny, nx, cnt+1});
                    vi[ny][nx] = true; 
                }
            }
        }
        return ans;
    }
};
