class NumMatrix {
private:
    vector<vector<int>> sum;
public:
    NumMatrix(vector<vector<int>>& matrix) {
        //if(matrix == {{}})
        //    return;
        int h = matrix.size();
        if(h==0)
            return;
        int w = matrix[0].size();
        sum = vector<vector<int>>(h+1, vector<int>(w+1, 0));
        for(int i=0; i<h; i++)
            for(int j=0; j<w; j++)
                sum[i+1][j+1] = matrix[i][j];
        
        for(int i=0; i<h+1; i++){
            for(int j=1; j<w+1; j++){
                sum[i][j] += sum[i][j-1];
            }
        }
        for(int j=0; j<w+1; j++){
            for(int i=1; i<h+1; i++){
                sum[i][j] += sum[i-1][j];
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        row1++;col1++;row2++;col2++;
        return sum[row2][col2] - sum[row2][col1-1] - sum[row1-1][col2] + sum[row1-1][col1-1];   
    }
};
