#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int arr[200001];
    int n;
    cin >> n;
    int whole = 0;
    for(int i=0; i<n; i++){
        cin >> arr[i];
        whole ^= arr[i];
    }
    for(int i=0; i<n; i++){
        cout << (arr[i]^whole) << ' ';
    }
    
    
    return 0;
}
