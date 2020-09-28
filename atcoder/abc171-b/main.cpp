#include <bits/stdc++.h>

using namespace std;

int main()
{
    int arr[1000];
    int n, k;
    cin >> n >> k;
    for(int i=0; i<n; i++){
        cin >> arr[i];
    }
    sort(arr, arr+n);
    int ans = 0;
    for(int i=0; i<k; i++)
        ans += arr[i];
    cout << ans;
    return 0;
}
