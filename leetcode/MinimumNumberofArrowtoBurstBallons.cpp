class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if(points.size() == 0)
            return 0;
        sort(points.begin(), points.end());
        int s = points[0][0];
        int e = points[0][1];
        int ans = 1;
        
        for(int i=1; i<points.size(); i++){
            int ss = points[i][0];
            int ee = points[i][1];
            if(ss <= e){ // overlapped
                s = ss;
                e = min(e, ee);
            }
            else{
                ans++;
                s = ss;
                e = ee;
            }
        }
        return ans;
    }
};
