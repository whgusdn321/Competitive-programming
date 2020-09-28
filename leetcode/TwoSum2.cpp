class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int s = numbers.size()-1;
        // for(int i=0; i<numbers.size(); i++)
        //     if(numbers[i] > target){
        //         s = i-1;
        //         break;
        //     }
        
        vector<int> ans;
        for(int r_ = s; r_>=1; r_--){
            int r = r_-1;
            int l = 0;
            while(l <= r){
                int m = (l+r)/2;
                // cout << "r is : " << r << " l is : " << l << " m is : " << m << '\n';
                if(numbers[m] + numbers[r_] == target){
                    ans = {m+1, r_+1};
                    break;
                }
                else if(numbers[m] + numbers[r_] < target){
                    l = m + 1;
                }
                else{
                    r = m - 1;
                }
            }
        }
        return ans;
    }
};
