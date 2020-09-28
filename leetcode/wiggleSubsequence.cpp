class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        if(nums.size() < 2){
            return nums.size();
        }
        int ans = 1;
        
        int last = 0;
        for(int i=1; i<nums.size(); i++){
            int cur = nums[i-1] - nums[i];
            if(last == 0 && cur != 0){
                last = cur;
                ans++;
            }
            else if(last*cur < 0){
                last = cur;
                ans++;
            }
           
        }
        return ans;
    }
};
