class Solution {
public:
    int minSteps(int nn) {
        queue<vector<int>> qu;
        //bool vi[1001];
        qu.push({1, 0, 0});
        //vi[1] = true;
        map<pair<int, int>, bool> vi; 
        vi[{1, 0}] = true;
        int ans = 0;
        while(!qu.empty()){
            auto tmp = qu.front();
            qu.pop();
            int n = tmp[0];
            int f = tmp[1];
            int cnt = tmp[2];
            if(n == nn){
                ans = cnt;
                break;
            }
            if(n+f<= 1000 && !vi[{n, f}]){
                qu.push({n+f, f, cnt+1});
                //vi[n+f] = true;
                vi[{n, f}] = true;
            }
            if(f != n){
                qu.push({n, n, cnt+1});
                //vi[n*2] = true;
            }
        }
        return ans;
    }
};
