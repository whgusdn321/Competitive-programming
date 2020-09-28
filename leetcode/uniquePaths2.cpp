class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int y = obstacleGrid.size();
        int x = obstacleGrid[0].size();
        vector<vector<int>> m(y, vector<int>(x, 0));
        for(int i=0; i<y; i++){
            if(obstacleGrid[i][0] == 0)    
                m[i][0] = 1;
            else
                break;
        }
        for(int j=0; j<x; j++){
            if(obstacleGrid[0][j] == 0)    
                m[0][j] = 1;
            else
                break;
        }
        for(int i=1; i<y; i++){
            for(int j=1; j<x; j++){
                if(obstacleGrid[i][j] == 0)
                    m[i][j] = m[i-1][j] + m[i][j-1];
                else
                    m[i][j] = 0;
            }
        }
        return m[y-1][x-1];
    }
};
