#include <bits/stdc++.h>

using namespace std;

int main()
{
    int tc;
    cin >> tc;
    int a[3], b[3];
    for(int t=0; t<tc; t++){
        int ans = 0;
        cin >> a[0] >> a[1] >> a[2];
        cin >> b[0] >> b[1] >> b[2];
        int c = min(a[2], b[1]);
        ans += 2*c;
        a[2] -= c;
        b[1] -= c;
        c = min(a[0], b[2]);
        a[0] -= c;
        b[2] -= c;
        c = min(a[2], b[2]);
        a[2] -= c;
        b[2] -= c;
        c = min(a[1], b[0]);
        a[1] -= c;
        b[0] -= c;
        c = min(a[1], b[1]);
        a[1] -= c;
        b[1] -= c;
        ans -= 2*min(a[1], b[2]);
        cout << ans << '\n';
        // cout << a[0] << ' ' << a[1] << ' ' << a[2] << '\n';
        // cout << b[0] << ' ' << b[1] << ' ' << b[2] << '\n';
    }
    return 0;
}
