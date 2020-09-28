#include <bits/stdc++.h>

using namespace std;

int main()
{
    int tc;
    cin >> tc;
    for(int i=0; i<tc; i++){
        int n;
        cin >> n;
        if(n%2){//odd
            cout << 1 + n/2 << '\n';
        }
        else{
            cout << n/2 << '\n';
        }
    }
    return 0;
}
