#include <bits/stdc++.h>

using namespace std;

int a[100000];

void solve(){
    int n, x;
    cin >> n >> x;
    int sum =0;
    for(int i=0; i<n; i++){
        cin >> a[i];
        sum += a[i];
    }
    int i = 0;
    int j = n-1;
    if(sum % x != 0){
        cout << n << '\n';
        return;
    }
    while(i < n){
        if(a[i] % x != 0){
            break;
        }
        i++;
    }
    while(j >= 0){
        if(a[j] % x != 0){
            break;
        }
        j--;
    }
    if(i <= j){
        cout << max(max(n-(i+1), i), max(j, n-(j+1))) << '\n';
    }
    else{
        cout << -1 << '\n';
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while(t){
        solve();
        t--;
    }
    return 0;
}
