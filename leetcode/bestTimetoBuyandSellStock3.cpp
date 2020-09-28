class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if(n==0) return 0;
        
        vector<int> lefts(n, 0), rights(n, 0);  
        
        int min_val = prices[0];
        int max_val = 0;
        for(int i=0; i<n; i++){
            if(prices[i] < min_val){
                min_val = prices[i];
            }
            else{
                max_val = max(max_val, prices[i] - min_val);
            }
            lefts[i] = max_val;
        } 
        int max_height = prices[n-1];
        max_val = 0;
        for(int j=n-1; j>=0; j--){
            if(prices[j] > max_height){
                max_height = prices[j];
            }
            else{
                max_val = max(max_val, max_height - prices[j]);
            }
            rights[j] = max_val;
        }
        // for(int i=0; i<n; i++){
        //     cout << lefts[i] << ' ';
        // }
        // cout << '\n';
        // for(int j=0; j<n; j++){
        //     cout << rights[j] << ' ';
        // }
        // cout << '\n';
        vector<int> ans(n, 0);
        for(int i=0; i<n; i++){
            ans[i] = lefts[i] + rights[i];
        }
        return *max_element(ans.begin(), ans.end());
    }
};
