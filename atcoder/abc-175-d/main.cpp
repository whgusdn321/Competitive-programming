#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, k;
    int p[5001];
    int c[5001];
    long long ans[5001] = {0};
    
    cin >> n >> k;
    for(int i=0; i<n; i++)
        cin >> p[i];
    for(int i=0; i<n; i++)
        cin >> c[i];  
        
    for(int i=0; i<n; i++){
        // find out length, cycle_length, cycle_sum, whole_sum, max_val, s_pos
        int length=0, cycle_length=0, s_pos=0;
        long long cycle_sum=0, whole_sum=0, max_val = -1e18;
        int s = i;
        
        unordered_map<int, vector<long long>> dict;
        while(dict[s].empty()){
            dict[s] = {length, whole_sum};
            length++;
            whole_sum += c[p[s]-1];
            s = p[s]-1;
            if(length <= k)
                max_val = max(whole_sum, max_val);
        }
        
        
        cycle_length = length - dict[s][0];
        cycle_sum = whole_sum - dict[s][1];
        s_pos = s;
        if(k <= length){
            ans[i] = max_val;
        }
        else{ // k > length
            if(cycle_sum <= 0)
                ans[i] = max_val;
            else{
                int pos_cycle = (k - length)/cycle_length;
                if(pos_cycle >= 1){
                    int left_k = (k-length) - (pos_cycle-1)*cycle_length;
                    whole_sum += (pos_cycle-1)*cycle_sum;
                    max_val = max(whole_sum, max_val);
                    for(int j=0; j<left_k; j++){
                        whole_sum += c[p[s_pos]-1];
                        s_pos = p[s_pos]-1;
                        max_val = max(whole_sum, max_val);
                    }
                    ans[i] = max_val;
                }
                else{
                    int left_k = k - length;
                    for(int j=0; j<left_k; j++){
                        whole_sum += c[p[s_pos]-1];
                        s_pos = p[s_pos]-1;
                        max_val = max(whole_sum, max_val);
                    }
                    ans[i] = max_val;
                }
            }
        }
    }
    cout << *max_element(ans, ans+n);
    return 0;
}

