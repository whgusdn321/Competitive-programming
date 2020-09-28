#include <bits/stdc++.h>

using namespace std;

int main()
{
    int tc;
    int arr[50001];
    cin >> tc;
    for(int t=0; t<tc; t++){
        int n;
        cin >> n;
        for(int i=0; i<n; i++)
            cin >> arr[i];
        if(arr[0] + arr[1] > arr[n-1]){
            cout << -1 << '\n';
        }
        else{
            cout << "1 2 " << n << '\n';
        }
    }
    return 0;
}
