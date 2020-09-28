#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    int arr[101];
    cin >> n;
    for(int i=0; i<n; i++)
        cin >> arr[i];
    sort(arr, arr+n);
    
    int ans = 0;
    for(int i=0; i<n; i++)
        for(int j=i+1; j<n; j++)
            for(int k=j+1; k<n; k++){
                if(arr[i] != arr[j] && arr[j] != arr[k] && arr[i] != arr[k] 
                && arr[i] + arr[j] > arr[k])
                    ans++;
            }
    cout << ans;
    return 0;
}
