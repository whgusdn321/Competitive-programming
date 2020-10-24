class Solution {
public:
    vector<int> asteroidCollision(vector<int>& a) {
        vector<int> vec;
        int n = a.size();
        for(int i=0; i<n; i++){
            if(a[i] < 0){
                while(!vec.empty() && vec.back() > 0 && abs(vec.back()) < abs(a[i])){
                    vec.pop_back();
                }
                if(!vec.empty() && vec.back() > 0 && abs(vec.back())==abs(a[i]) ){
                    vec.pop_back();
                }
                else if(!vec.empty() && vec.back() > 0){
                    continue;
                }
                else{
                    vec.push_back(a[i]);
                }
            }
            else{
                vec.push_back(a[i]);
            }
        }
        return vec;
    }
};
