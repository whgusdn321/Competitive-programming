#include <bits/stdc++.h>

using namespace std;

int main()
{
    int tc;
    cin >> tc;
    for(int t=0; t<tc; t++){
        int n, k;
        cin >> n >> k;
        if(k <= n){
            if(k%2 == n%2)
                cout << 0 << '\n';
            else
                cout << 1 << '\n';
        }
        else{
            cout << k - n << '\n';
        }
    }
    return 0;
}
