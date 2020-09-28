#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int i=0; i<t; i++){
        int n;
        cin >> n;
        // long double t = 180/(360.0/n);
        // long long tt = 180/(360.0/n);
        if(n%4 == 0)
            cout << "YES" << '\n';
        else
            cout << "NO" << '\n';
        // cout << 180.0 / (360.0/n) << '\n';
        //if(180.0 / (360.0/n) == 0)
        //    cout << "YES" << '\n';
        //else
        //    cout << "NO" << '\n';
    }
    return 0;
}
