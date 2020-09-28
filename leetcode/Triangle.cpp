class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        vector<int> memo = triangle.back();
        for(int i=triangle.size()-2; i>=0; i--){
            vector<int> row= triangle[i];
            for(int j=0; j<row.size(); j++){
                memo[j] = min(memo[j] + row[j], memo[j+1] + row[j]);
            }
        }
        return memo[0];
    }
};
