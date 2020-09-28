class Solution {
public:
    int ans;
    void go(int n, int cnt, vector<int> &visited){
        if(n == 0){
            ans = min(ans, cnt);
            return;
        }
        if(n < 0){
            return;
        }
        int num = 1;
        while(n >= (num+1)*(num+1)){
            num++;
        }
        
        while(num >= 1){
            //cout << "n is : " << n <<" num is : " << num << '\n';
            if(cnt < ans){
                if(!visited[n-num*num] || visited[n-num*num] > cnt){
                    visited[n-num*num] = cnt;
                    go(n-num*num, cnt+1, visited);
                }
            }
            num--;
        }
        return;
    }
    int numSquares(int n) {
        vector<int> visited(n+1, 0);    
        ans = n;
        go(n, 0, visited);
        return ans;
    }
};
