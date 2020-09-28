#include <bits/stdc++.h>

using namespace std;

int main()
{
    int tc;
    cin >> tc;
    int a, b;
    for(int t=0; t<tc; t++){
        cin >> a >> b;
        int diff = abs(a-b);
        if (diff%10)
            cout << diff/10+1 << '\n';
        else
            cout << diff/10  << '\n';
    }
    return 0;
}
