class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int h = matrix.size();
        if(!h)
            return false;
        int w = matrix[0].size();
        if(!w)
            return false;
        
        int l = 0;
        int r = h-1;
        
        while(l <= r){
            int m = (l+r)/2;
            if(matrix[m][0] <= target){
                l = m+1;
            }
            else{
                r = m-1;
            }
        }
        int ll = 0;
        int rr = w-1;
        bool pos = false;
        if(l != h)
            while(ll <= rr){
                int m = (ll+rr)/2;
                if(matrix[l][m] < target){
                    ll = m+1;
                }
                else if(matrix[l][m] > target){
                    rr = m-1;
                }
                else{
                    pos = true;
                    break;
                }
            }
        
        ll = 0;
        rr = w-1;
        if(r != -1)
            while(ll <= rr){
                int m = (ll+rr)/2;
                if(matrix[r][m] < target){
                    ll = m+1;
                }
                else if(matrix[r][m] > target){
                    rr = m-1;
                }
                else{
                    pos = true;
                    break;
                }
            }
        return pos;
    }
};
