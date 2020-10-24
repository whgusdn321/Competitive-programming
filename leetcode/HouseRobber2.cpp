class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp1, dp2;
        if(n==1)
            return nums[0];
        if(n==2)
            return max(nums[0], nums[1]);
        dp1=nums;
        dp2=nums;
       
        dp1[2] += dp1[0];
        if(n==3)
            return max({nums[0], nums[1], nums[2]});
        
        dp1[3] += dp1[0];
        dp2[3] += dp2[1];
        if(n==4)
            return max({dp1[2], dp2[3]});
        
        dp1[4] += dp1[2];
        for(int i=5; i<n-1; i++){
            dp1[i] += max(dp1[i-2], dp1[i-3]);
        }
        
        for(int i=4; i<n; i++){
            dp2[i] += max(dp2[i-2], dp2[i-3]);
        }
        return max({dp1[n-2], dp1[n-3], dp2[n-1], dp2[n-2]});
        
    }
};
