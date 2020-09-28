#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T = 0;
    cin >> T;
    for(int tc=0; tc<T; tc++){
        int n, x, m;
        cin >> n >> x >> m;
        int ll= x, rr = x;
        int ans = 1;
        for(int i=0; i<m; i++){
            int l, r;
            cin >> l >> r;
            if(!((l > rr) || (r < ll))){
                ll = min(l, ll);
                rr = max(r, rr);
            }
            else{
                continue;
            }
        }
        
        cout << rr - ll + 1 << '\n';
    }
    return 0;
}