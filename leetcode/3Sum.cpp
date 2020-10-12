class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<int> pos, neg;
        unordered_map<int, bool> pm, nm;
        int zeros = 0;
        for(int num : nums){
            if(num >= 0){
                pos.push_back(num);
                pm[num] = true;
                if(num == 0)
                    zeros++;
            }
            else{
                neg.push_back(num);
                nm[num] = true;
            }
        }
        //pC1*nC2 first
        sort(pos.begin(), pos.end());
        sort(neg.begin(), neg.end());
        set<vector<int>> ans;
        for(int i=0; i<neg.size(); i++){
            for(int j=i+1; j<neg.size(); j++){
                int tmp = neg[i] + neg[j];
                int need = -(tmp);
                if(pm[need]){
                    ans.insert({neg[i], neg[j], need});
                }
            }
        }
        //nC1*pC2 next
        for(int i=0; i<pos.size(); i++){
            for(int j=i+1; j<pos.size(); j++){
                int tmp = pos[i] + pos[j];
                int need = -(tmp);
                if(nm[need]){
                    ans.insert({pos[i], pos[j], need});
                }
            }
        }
        vector<vector<int>> ret;
        for(auto it=ans.begin(); it!=ans.end(); it++){
            ret.push_back(*it);
        }
        if(zeros>=3)
            ret.push_back({0,0,0});
        return ret;
        
    }
};
