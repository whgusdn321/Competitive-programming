#include <bits/stdc++.h>

using namespace std;

int a[200001];
int w[200001];

void solve(){
    int n, k;
    int ones = 0;
    cin >> n >> k;
    for(int i=0; i<n; i++)
        cin >> a[i];
    for(int i=0; i<k; i++){
        cin >> w[i];
        if(w[i]==1) ones++;
    }
    sort(a, a+n);
    sort(w, w+k, greater<int>());
    int tmp[200001];
    for(int j=0; j<n-ones; j++){
        tmp[j+ones] = w[j];
    }
    for(int j=0; j<ones; j++){
        tmp[j] = 1;
    }
    // cout << "tmp is : ";
    // for(int i=0; i<k; i++){
    //     cout << tmp[i] << ' ';
    // }
    // cout << '\n';
    int left = 0, right = n-1;
    long long ans = 0;
    for(int i=0; i<k; i++){
        int num = tmp[i];
        if(num == 1){
            ans += a[right]*2;
            right--;
        }
        else if(num == 2){
            ans += (a[right] + a[left]);
            right--;
            left++;
        }
        else{ // num >= 3
            ans += (a[right] + a[left]);
            right--;
            left++;
            num -= 2;
            while(num > 0){
                left++;
                num-=1;
            }
        }
    }
    cout << ans << '\n';
    
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int tc;
    cin >> tc;
    while(tc > 0){
        solve();
        tc--;
    }
    return 0;
}
