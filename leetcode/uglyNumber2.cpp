class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> vec = {1};
        int idx1=0, idx2=0, idx3=0;
        
        while(vec.size() < 1690){
            int n = min({vec[idx1]*2, vec[idx2]*3, vec[idx3]*5});
            vec.push_back(n);
            if(n == vec[idx1]*2){
                idx1++;
            }
            if(n == vec[idx2]*3){
                idx2++;
            }
            if(n == vec[idx3]*5){
                idx3++;
            }
        }
        
        // for(int x : vec)
        //     cout << x << ' ';
        // cout <<'\n';    
        return vec[n-1]; 
    }
};
