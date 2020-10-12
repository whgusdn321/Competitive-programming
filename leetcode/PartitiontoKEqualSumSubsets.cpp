class Solution {
public:
    bool f(int i, vector<int> &nums, vector<int> &groups, int target){
        bool pos = false;
        if(i >= nums.size())
            return true;
        
        for(int j=0; j<groups.size(); j++){
            if(pos)
                break;
            if(groups[j] + nums[i] <= target){
                groups[j] += nums[i];
                pos |= f(i+1, nums, groups, target);
                groups[j] -= nums[i];
            }
        }
        return pos;
    }
    
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int sum = 0;
        for(int n : nums)
            sum += n;
        if(sum % k != 0)
            return false;
        int target = sum / k;
        for(int n : nums){
            if(n > target)
                return false;
        }
        //cout << target<< '\n';
        vector<int> groups(k, 0);
        sort(nums.begin(), nums.end(), greater<int>());
        return f(0, nums, groups, target);
    }
};
