#include <bits/stdc++.h>

using namespace std;

int main()
{
    string s;
    cin >> s;
    int rain = 0;
    int ans = -99;
    for(int i=0; i<3; i++)
        if(s[i] == 'R'){
            rain++;
            if(i == 2)
                ans = max(ans, rain);
        }
        else{
            ans = max(ans, rain);
            rain = 0;
        }
    cout << ans << '\n';
    return 0;
}
