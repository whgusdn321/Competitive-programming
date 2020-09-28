class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> dict;
        
        vector<int> ans;
        for(int i=0; i<nums.size(); i++){
            int num = nums[i];
            int needed = target - num;
            if(dict[needed]){
                ans = {i, dict[needed]-1}; 
                break;
            }
            else{
                dict[num] = i+1;
            }
        }
        return ans;
    }
};
