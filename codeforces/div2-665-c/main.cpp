#include <bits/stdc++.h>

using namespace std;

long long arr[100001];
long long b[100001];
long long n;

bool cmp(const long long a1, const long long a2){
    return arr[a1] <= arr[a2];
}

int main()
{
    long long tc;
    cin >> tc;
    for(long long t=0; t<tc; t++){
        cin >> n;
        for(long long i=0; i<n; i++){
            cin >> arr[i];
            b[i] = arr[i];
        }
        long long min = *min_element(arr, arr+n);    
        vector<long long> idxs, idxs_cpy;
        for(long long i=0; i<n; i++){
            if(arr[i] % min == 0){
                idxs.push_back(i);
            }
        }
        
        idxs_cpy = idxs;
        sort(idxs.begin(), idxs.end(), cmp);
        for(long long i=0; i<idxs.size(); i++){
            long long orign = idxs_cpy[i];
            long long changed = idxs[i];
            b[orign] = arr[changed];
        }
        long long before = -1;
        bool pos = true;
        for(long long i=0; i<n; i++){
            if(b[i] >= before){
                before = b[i];
            }
            else{
                pos = false;
                break;
            }
        }
        if(pos)
            cout << "YES" << '\n';
        else
            cout << "NO" << '\n';
    }
    return 0;
}
