class Solution {
public:
    int candy(vector<int>& ratings) {
        vector<int> ans(ratings.size(), 0);
        if(ratings.empty())
            return 0;
        if(ratings.size() == 1){
            return 1;
        }
        for(int i=1; i<ratings.size(); i++){
            if(ratings[i] > ratings[i-1]){
                if(ans[i-1] == 0){
                    ans[i-1] = 1;
                }
                ans[i] = ans[i-1] + 1;
            }
            else{
                continue;
            }
        }
        if(ans.back() == 0)
            ans[ans.size()-1] = 1;
        
        for(int i=ans.size()-1; i>=0; i--){
            if(ans[i] == 0 && ratings[i] > ratings[i+1]){
                ans[i] = ans[i+1] + 1;
            }
            else if(ans[i] == 0 && ratings[i] == ratings[i+1])
                ans[i] = 1;
            else{;}
        }
        for(int i=1; i<ans.size()-1; i++){
            if(ratings[i] > ratings[i-1] && ratings[i] > ratings[i+1]){
                if(ans[i] > ans[i-1] && ans[i] > ans[i+1])
                    continue;
                else
                    ans[i] = max(ans[i-1], ans[i+1]) + 1;
            }
        }
        //for(int i=0; i<ans.size(); i++)
        //    cout << ans[i] << ' ';
        //cout << '\n';
        int sum = 0;
        for(int i=0; i<ans.size(); i++){
            sum += ans[i];
        }
        return sum;
    }
};
