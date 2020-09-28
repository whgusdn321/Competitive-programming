#include <bits/stdc++.h>

using namespace std;

int arr[1000000];

void solve(){
    int n;
    cin >> n;
    for(int i=0; i<n; i++){
        cin >> arr[i];
    }
    int sign;  
    if(arr[1] - arr[0] > 0)
        sign = 1;
    else
        sign = -1;
    vector<int> vec;
    vec.push_back(0);
    
    int i = 0, j = 1;
    while(i < n-1){
        int tmp = arr[j] - arr[i];
        if(tmp * sign >= 0){
            i++;
            j++;
        }
        else {
            vec.push_back(i);
            sign *= -1;
            i++;
            j++;
        }
    }
    vec.push_back(n-1);
    cout << vec.size() << '\n';
    for(int x : vec)
        cout << arr[x] << ' ';
    cout << '\n';
    
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
