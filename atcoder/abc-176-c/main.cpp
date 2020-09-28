#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    int arr[200001];
    cin >> n;
    for(int i=0; i<n; i++){
        cin >> arr[i];
    }
    long long ans = 0;
    for(int i=1; i<n; i++){
        if(arr[i] >= arr[i-1])
            continue;
        else{
            ans += arr[i-1] - arr[i];
            arr[i] = arr[i-1];
        } 
    }
    // for(int i=0; i<n; i++)
    //     cout << arr[i] << ' ';
    // cout << '\n';
    cout << ans << '\n';
    return 0;
}
