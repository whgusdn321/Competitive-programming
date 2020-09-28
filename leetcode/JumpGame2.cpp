#include <bits/stdc++.h>

class Solution {
public:
    
    bool cj(int idx, vector<int>& nums, vector<int>& memo){
        bool pos = false;
        if(idx == nums.size() -1)
            return true;
        
        int limit = min(idx+nums[idx], (int)nums.size()-1);
        for(int next = idx+1; next <= limit ; next++){
            if(memo[next] != 2)
                pos |= memo[next];
            else{
                bool tmp = cj(next, nums, memo);
                memo[next] = tmp;
                pos |= tmp;
            }
        }
        return pos;
    }
    
    bool canJump(vector<int>& nums) {
        int cnt = 1;
        int n = nums.size();
        if(n==1)
            return true;
        vector<int> memo(n, 2);
        return cj(0, nums, memo);
        
    }
};

