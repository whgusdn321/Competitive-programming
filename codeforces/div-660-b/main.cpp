#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int tc, n;
    cin >> tc;
    for(int i=0; i<tc; i++){
        cin >> n;
        int c = (n-0.0001)/4 + 1;
        for(int j=0; j<n-c; j++)
            cout <<9;
        for(int j=0; j<c; j++)
            cout <<8;
        cout << '\n';
    }
    return 0;
}
