class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.empty()){
            return 0;
        }
        if(nums.size() <= 3){
            return *max_element(nums.begin(), nums.end());
        }
        vector<int> nums2 = nums;
        for(int i=nums.size()-4; i >= 0; i--){
            if(i+3 < nums.size()-1){
                nums[i] += max(nums[i+2], nums[i+3]);
            }
            else{
                nums[i] += nums[i+2];
            }
        }
        
        for(int i=nums2.size()-3; i>=1; i--){
            if(i+3 < nums2.size()){
                nums2[i] += max(nums2[i+2], nums2[i+3]);
            } 
            else{
                nums2[i] += nums2[i+2];
            }
        }
        return max({nums[0], nums[1], nums2[1], nums2[2]});
    }
};
