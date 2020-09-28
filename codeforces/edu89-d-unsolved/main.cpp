#include <bits/stdc++.h>

using namespace std;

int a[1000000];
int b[1000000];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m;
    cin >> n >> m;
    for(int i=0; i<n; i++){
        cin >> a[i];
    }
    for(int i=0; i<m; i++){
        cin >> b[i];
    }
    
    int i = n-1;
    int j = m-1;
    int jval = b[j];
    while(i >= 0){ // 안되는 경우 먼저 검사
        if(a[i] >= jval){
            if(a[i] == jval){
                j--;
                if(j >=0)
                    jval = b[j];
            }
            i--;
        }
        else{
            cout << 0 << '\n';
            return 0;
        }
    }
    if(j >= 0){
        cout << 0 <<'\n';
        return 0;
    }
    map<int, long long> dict;
    int min = 1000000000 + 1;
    for(int i=n-1; i>=0; i--){
        if(min>a[i])
            min = a[i];
        dict[min]++;
    }
    
    long long ans = 1;
    for(int i=m-1; i>0; i--){
        ans *= (dict[b[i]] % 998244353);
        ans %= 998244353;
    }
    cout << ans << '\n';
    return 0;
    
}
