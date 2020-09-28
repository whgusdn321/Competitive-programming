#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int tc;
    cin >> tc;
    int a[100];
    int b[100];
    for(int t=0; t<tc; t++){
        int n;
        cin >> n;
        for(int i=0; i<n; i++){
            cin >> a[i];
        }
        for(int i=0; i<n; i++){
            cin >> b[i];
        }
        int amin = *min_element(a, a+n);
        int bmin = *min_element(b, b+n);
        long long ans = 0;
        for(int i=0; i<n; i++){
            int a_r = a[i] - amin;
            int b_r = b[i] - bmin;
            int k = min(a_r, b_r);
            ans += k;
            a_r -= k;
            b_r -= k;
            ans += (a_r + b_r);
        }
        cout << ans << '\n';
    }
    return 0;
}
