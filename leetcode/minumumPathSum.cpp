class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int y = grid.size();
        int x = grid[0].size();
        
        for(int i=1; i<y; i++)
            grid[i][0] = grid[i-1][0] + grid[i][0];
        for(int j=1; j<x; j++)
            grid[0][j] = grid[0][j-1] + grid[0][j];
        for(int i=1; i<y; i++){
            for(int j=1; j<x; j++){
                grid[i][j] = min(grid[i-1][j] + grid[i][j], grid[i][j-1] + grid[i][j]);
            }
        }
        return grid[y-1][x-1];
    }
};
