#include <bits/stdc++.h>

using namespace std;

int main()
{
    long long n;
    cin >> n;
    char ch = 'a' - 1;
    string ans = "";
    while(n){
        int lefted = n % 26;
        n = n/26;
        if(lefted > 1)
            ans += (ch + lefted);
        else
            ans += ch + 'z';
    } 
    reverse(ans.begin(), ans.end());
    cout << ans << '\n';
    return 0;
}