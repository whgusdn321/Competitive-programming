#include <bits/stdc++.h>

using namespace std;

int main()
{
    int tc;
    cin >> tc;
    for(int t=0; t<tc; t++){
        int n;
        cin >> n;
        if(n<=2)
            cout << n << '\n';
        else
            cout << n/2+1 << '\n';
    }
    return 0;
}
