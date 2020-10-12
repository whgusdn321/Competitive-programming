class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        unordered_map<int, vector<int>> dict;
        map<vector<int>, bool> vi;
        
        for(int i=0; i<nums.size(); i++){
            dict[nums[i]].push_back(i);
        }
        int n = nums.size();
        
        for(int i=0; i<n; i++){
            for(int j=i+1; j<n; j++){
                for(int l=j+1; l<n; l++){
                    int a = nums[i] + nums[j] + nums[l];
                    int wanted = target-a;
                    for(int idx : dict[wanted]){
                        if(idx!=i && idx!=j && idx!=l){
                            vector<int> tmp = {nums[i], nums[j], nums[l], nums[idx]};
                            sort(tmp.begin(), tmp.end());
                            if(!vi[tmp]){
                                ans.push_back(tmp);
                                vi[tmp] = true;
                                break;
                            }
                        }
                    }
                }
            }
        }
        return ans;
    }
};
