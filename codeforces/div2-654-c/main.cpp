#include <bits/stdc++.h>

using namespace std;

int main()
{
    int tc;
    cin >> tc;
    for(int i=0; i<tc; i++){
        long long a, b, n, m;
        cin >> a >> b >> n >> m;
        if(n+m <= a + b && m <= min(a, b))
            cout << "Yes" << '\n';
        else
            cout << "No" << '\n';
    }
    return 0;
}
