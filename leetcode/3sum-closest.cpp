class Solution {
public:
    int threeSumClosest(vector<int>& n, int target) {
        sort(n.begin(), n.end());
        int ans = 1e6;
        for(int i=0; i<n.size(); i++){
            for(int j=i+1; j<n.size(); j++){
                int l = j+1;
                int r = n.size() - 1;
                if(l <n.size() && r < n.size()){
                    while(l < r-1){
                        int mid = (l+r)/2;
                        if(n[i]+n[j]+n[mid] >= target)
                            r = mid;
                        else
                            l = mid;
                    }
                    if(abs(target-(n[i]+n[j]+n[l])) < abs(target - ans)){
                        ans = n[i]+n[j]+n[l];
                        //cout << i << j << l << ' ' << ans << '\n';
                    }
                    if(abs(target-(n[i]+n[j]+n[r])) < abs(target - ans)){
                        ans = n[i]+n[j]+n[r];
                        //cout << i << j << r << ' ' << ans << '\n';
                    }
                }
            }
        }
        return ans;
    }
};
